"""Unit tests for Cherry Servers Python SDK projects client."""

from __future__ import annotations

from typing import Any, cast
from unittest import mock

import cherryservers_sdk_python.projects
from tests.unit import helpers


def test_get_by_id_success(
    simple_project: dict[str, Any],
    projects_client: cherryservers_sdk_python.projects.ProjectClient,
) -> None:
    """Test successfully getting project by ID."""
    expected_api_resp = helpers.build_api_response(simple_project, 200)
    cast(mock.Mock, projects_client._api_client.get).return_value = expected_api_resp
    project = projects_client.get_by_id(simple_project["id"])

    assert (
        project.get_model()
        == cherryservers_sdk_python.projects.ProjectModel.model_validate(simple_project)
    )

    cast(mock.Mock, projects_client._api_client.get).assert_called_with(
        f"projects/{simple_project['id']}",
        None,
        projects_client.request_timeout,
    )


def test_list_by_team_success(
    simple_project: dict[str, Any],
    projects_client: cherryservers_sdk_python.projects.ProjectClient,
) -> None:
    """Test successfully listing all team projects."""
    expected_api_resp = helpers.build_api_response(
        [simple_project, simple_project], 200
    )
    cast(mock.Mock, projects_client._api_client.get).return_value = expected_api_resp
    projects = projects_client.list_by_team(123456)

    for project, expected_project in zip(projects, [simple_project, simple_project]):
        assert (
            project.get_model()
            == cherryservers_sdk_python.projects.ProjectModel.model_validate(
                expected_project
            )
        )

    cast(mock.Mock, projects_client._api_client.get).assert_called_with(
        "teams/123456/projects", None, projects_client.request_timeout
    )


def test_create_success(
    simple_project: dict[str, Any],
    projects_client: cherryservers_sdk_python.projects.ProjectClient,
) -> None:
    """Test successfully creating a project."""
    creation_schema = cherryservers_sdk_python.projects.CreationRequest(
        name="test", bgp=True
    )

    get_response = helpers.build_api_response(simple_project, 200)
    post_response = helpers.build_api_response(simple_project, 201)
    cast(mock.Mock, projects_client._api_client.post).return_value = post_response
    cast(mock.Mock, projects_client._api_client.get).return_value = get_response

    project = projects_client.create(creation_schema, 123456)

    assert (
        project.get_model()
        == cherryservers_sdk_python.projects.ProjectModel.model_validate(simple_project)
    )

    cast(mock.Mock, projects_client._api_client.post).assert_called_with(
        "teams/123456/projects", creation_schema, None, projects_client.request_timeout
    )

    cast(mock.Mock, projects_client._api_client.get).assert_called_with(
        f"projects/{simple_project['id']}",
        None,
        projects_client.request_timeout,
    )


def test_update_success(
    simple_project: dict[str, Any],
    projects_client: cherryservers_sdk_python.projects.ProjectClient,
) -> None:
    """Test successfully updating a project."""
    update_req = cherryservers_sdk_python.projects.UpdateRequest(
        name=simple_project["name"],
        bgp=simple_project["bgp"]["enabled"],
    )

    cast(
        mock.Mock, projects_client._api_client.get
    ).return_value = helpers.build_api_response(simple_project, 200)
    cast(
        mock.Mock, projects_client._api_client.put
    ).return_value = helpers.build_api_response(simple_project, 201)

    sshkey = projects_client.update(simple_project["id"], update_req)

    assert (
        sshkey.get_model()
        == cherryservers_sdk_python.projects.ProjectModel.model_validate(simple_project)
    )

    cast(mock.Mock, projects_client._api_client.get).assert_called_once_with(
        f"projects/{simple_project['id']}",
        None,
        projects_client.request_timeout,
    )

    cast(mock.Mock, projects_client._api_client.put).assert_called_once_with(
        f"projects/{simple_project['id']}",
        update_req,
        None,
        projects_client._request_timeout,
    )


def test_delete_success(
    simple_project: dict[str, Any],
    projects_client: cherryservers_sdk_python.projects.ProjectClient,
) -> None:
    """Test successfully deleting a project."""
    cast(
        mock.Mock, projects_client._api_client.delete
    ).return_value = helpers.build_api_response({}, 204)

    projects_client.delete(simple_project["id"])

    cast(mock.Mock, projects_client._api_client.delete).assert_called_once_with(
        f"projects/{simple_project['id']}", None, projects_client._request_timeout
    )
