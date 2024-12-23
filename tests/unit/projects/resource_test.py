"""Unit tests for Cherry Servers Python SDK project resource."""

from __future__ import annotations

import copy
from typing import Any, cast
from unittest import mock

import cherryservers_sdk_python.projects
from tests.unit import helpers


def test_get_id(
    project_resource: cherryservers_sdk_python.projects.Project,
) -> None:
    """Test getting project resource ID."""
    assert project_resource.get_id() == project_resource.get_model().id


def test_update(
    project_resource: cherryservers_sdk_python.projects.Project,
    simple_project: dict[str, Any],
) -> None:
    """Test updating a project resource."""
    updated_project = copy.deepcopy(simple_project)
    updated_project["name"] = "updated-project"
    updated_project["bgp"]["enabled"] = False

    update_req = cherryservers_sdk_python.projects.UpdateRequest(
        name="updated-project", bgp=False
    )

    cast(
        mock.Mock, project_resource._client._api_client.get
    ).return_value = helpers.build_api_response(updated_project, 200)
    cast(
        mock.Mock, project_resource._client._api_client.put
    ).return_value = helpers.build_api_response(updated_project, 201)

    project_resource.update(update_req)

    assert (
        project_resource.get_model()
        == cherryservers_sdk_python.projects.ProjectModel.model_validate(
            updated_project
        )
    )

    cast(mock.Mock, project_resource._client._api_client.get).assert_called_once_with(
        f"projects/{simple_project['id']}",
        None,
        project_resource._client.request_timeout,
    )

    cast(mock.Mock, project_resource._client._api_client.put).assert_called_once_with(
        f"projects/{simple_project['id']}",
        update_req,
        None,
        project_resource._client._request_timeout,
    )


def test_delete(
    project_resource: cherryservers_sdk_python.projects.Project,
    simple_project: dict[str, Any],
) -> None:
    """Test deleting a project resource."""
    cast(
        mock.Mock, project_resource._client._api_client.delete
    ).return_value = helpers.build_api_response({}, 204)

    project_resource.delete()

    cast(
        mock.Mock, project_resource._client._api_client.delete
    ).assert_called_once_with(
        f"projects/{simple_project['id']}",
        None,
        project_resource._client._request_timeout,
    )
