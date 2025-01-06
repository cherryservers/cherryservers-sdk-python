"""Unit tests for Cherry Servers Python SDK teams client."""

from __future__ import annotations

from typing import Any, cast
from unittest import mock

import cherryservers_sdk_python.users
from tests.unit import helpers


def test_get_by_id_success(
    simple_team: dict[str, Any],
    teams_client: cherryservers_sdk_python.teams.TeamClient,
) -> None:
    """Test successfully getting a team by ID."""
    expected_api_resp = helpers.build_api_response(simple_team, 200)
    cast(mock.Mock, teams_client._api_client.get).return_value = expected_api_resp
    team = teams_client.get_by_id(simple_team["id"])

    assert team.get_model() == cherryservers_sdk_python.teams.TeamModel.model_validate(
        simple_team
    )

    cast(mock.Mock, teams_client._api_client.get).assert_called_with(
        f"teams/{simple_team['id']}",
        None,
        teams_client.request_timeout,
    )


def test_get_all_success(
    simple_team: dict[str, Any],
    teams_client: cherryservers_sdk_python.teams.TeamClient,
) -> None:
    """Test successfully getting all teams."""
    expected_api_resp = helpers.build_api_response([simple_team, simple_team], 200)
    cast(mock.Mock, teams_client._api_client.get).return_value = expected_api_resp
    teams = teams_client.get_all()

    for team, expected_team in zip(teams, [simple_team, simple_team], strict=False):
        assert (
            team.get_model()
            == cherryservers_sdk_python.teams.TeamModel.model_validate(expected_team)
        )

    cast(mock.Mock, teams_client._api_client.get).assert_called_with(
        "teams",
        None,
        teams_client.request_timeout,
    )


def test_create_success(
    simple_team: dict[str, Any],
    teams_client: cherryservers_sdk_python.teams.TeamClient,
) -> None:
    """Test successfully creating a team."""
    creation_schema = cherryservers_sdk_python.teams.CreationRequest(
        name="team", type="personal"
    )

    get_response = helpers.build_api_response(simple_team, 200)
    post_response = helpers.build_api_response(simple_team, 201)
    cast(mock.Mock, teams_client._api_client.post).return_value = post_response
    cast(mock.Mock, teams_client._api_client.get).return_value = get_response

    team = teams_client.create(creation_schema)

    assert team.get_model() == cherryservers_sdk_python.teams.TeamModel.model_validate(
        simple_team
    )

    cast(mock.Mock, teams_client._api_client.post).assert_called_with(
        "teams", creation_schema, None, teams_client.request_timeout
    )

    cast(mock.Mock, teams_client._api_client.get).assert_called_with(
        f"teams/{simple_team['id']}",
        None,
        teams_client.request_timeout,
    )


def test_update_success(
    simple_team: dict[str, Any],
    teams_client: cherryservers_sdk_python.teams.TeamClient,
) -> None:
    """Test successfully updating a team."""
    update_req = cherryservers_sdk_python.teams.UpdateRequest(name="team")

    cast(
        mock.Mock, teams_client._api_client.get
    ).return_value = helpers.build_api_response(simple_team, 200)
    cast(
        mock.Mock, teams_client._api_client.put
    ).return_value = helpers.build_api_response(simple_team, 201)

    team = teams_client.update(simple_team["id"], update_req)

    assert team.get_model() == cherryservers_sdk_python.teams.TeamModel.model_validate(
        simple_team
    )

    cast(mock.Mock, teams_client._api_client.get).assert_called_once_with(
        f"teams/{simple_team['id']}",
        None,
        teams_client.request_timeout,
    )

    cast(mock.Mock, teams_client._api_client.put).assert_called_once_with(
        f"teams/{simple_team['id']}",
        update_req,
        None,
        teams_client._request_timeout,
    )


def test_delete_success(
    simple_team: dict[str, Any],
    teams_client: cherryservers_sdk_python.teams.TeamClient,
) -> None:
    """Test successfully deleting a team."""
    cast(
        mock.Mock, teams_client._api_client.delete
    ).return_value = helpers.build_api_response({}, 204)

    teams_client.delete(simple_team["id"])

    cast(mock.Mock, teams_client._api_client.delete).assert_called_once_with(
        f"teams/{simple_team['id']}",
        None,
        teams_client._request_timeout,
    )
