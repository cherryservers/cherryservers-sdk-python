"""Unit tests for Cherry Servers Python SDK team resource."""

from __future__ import annotations

import copy
from typing import TYPE_CHECKING, Any, cast

import cherryservers_sdk_python.users
from tests.unit import helpers

if TYPE_CHECKING:
    from unittest import mock


def test_get_id(
    team_resource: cherryservers_sdk_python.teams.Team,
) -> None:
    """Test getting team resource ID."""
    assert team_resource.get_id() == team_resource.get_model().id


def test_update(
    team_resource: cherryservers_sdk_python.teams.Team,
    simple_team: dict[str, Any],
) -> None:
    """Test updating a team resource."""
    updated_team = copy.deepcopy(simple_team)
    assert isinstance(updated_team, dict)
    assert updated_team.get("name", None) is not None
    updated_team["name"] = "updated-team"

    update_req = cherryservers_sdk_python.teams.UpdateRequest(name="updated-team")

    cast(
        "mock.Mock", team_resource._client._api_client.get
    ).return_value = helpers.build_api_response(updated_team, 200)
    cast(
        "mock.Mock", team_resource._client._api_client.put
    ).return_value = helpers.build_api_response(updated_team, 201)

    team_resource.update(update_req)

    assert (
        team_resource.get_model()
        == cherryservers_sdk_python.teams.TeamModel.model_validate(updated_team)
    )

    cast("mock.Mock", team_resource._client._api_client.get).assert_called_once_with(
        f"teams/{simple_team['id']}",
        None,
        team_resource._client.request_timeout,
    )

    cast("mock.Mock", team_resource._client._api_client.put).assert_called_once_with(
        f"teams/{simple_team['id']}",
        update_req,
        None,
        team_resource._client._request_timeout,
    )


def test_delete(
    team_resource: cherryservers_sdk_python.teams.Team,
    simple_team: dict[str, Any],
) -> None:
    """Test deleting a team resource."""
    cast(
        "mock.Mock", team_resource._client._api_client.delete
    ).return_value = helpers.build_api_response({}, 204)

    team_resource.delete()

    cast("mock.Mock", team_resource._client._api_client.delete).assert_called_once_with(
        f"teams/{simple_team['id']}",
        None,
        team_resource._client._request_timeout,
    )
