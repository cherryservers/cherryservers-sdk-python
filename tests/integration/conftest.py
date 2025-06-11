"""Integration test configuration."""

from __future__ import annotations

import os
from typing import TYPE_CHECKING

import pytest

import cherryservers_sdk_python

if TYPE_CHECKING:
    from collections.abc import Generator


@pytest.fixture(scope="package")
def facade() -> cherryservers_sdk_python.facade.CherryApiFacade:
    """Initialize Cherry API facade."""
    token = os.environ.get("CHERRY_TEST_API_KEY")
    assert token, "CHERRY_TEST_API_KEY environment variable is not set"
    return cherryservers_sdk_python.facade.CherryApiFacade(
        token=token, user_agent_prefix="test"
    )


@pytest.fixture(scope="package")
def team_id() -> int:
    """Get a pre-initialized Cherry Servers team."""
    team_id = os.environ.get("CHERRY_TEST_TEAM_ID")
    assert team_id, "CHERRY_TEST_TEAM_ID environment variable is not set"
    return int(team_id)


@pytest.fixture(scope="package")
def project(
    team_id: int, facade: cherryservers_sdk_python.facade.CherryApiFacade
) -> Generator[cherryservers_sdk_python.projects.Project]:
    """Initialize a Cherry Servers project."""
    creation_req = cherryservers_sdk_python.projects.CreationRequest(
        name="cherryservers-python-sdk-project-fixture"
    )
    project = facade.projects.create(creation_req, team_id=team_id)
    yield project
    project.delete()


@pytest.fixture(scope="package")
def vps(
    facade: cherryservers_sdk_python.facade.CherryApiFacade,
    project: cherryservers_sdk_python.projects.Project,
) -> Generator[cherryservers_sdk_python.servers.Server]:
    """Initialize a Cherry Servers VPS."""
    creation_req = cherryservers_sdk_python.servers.CreationRequest(
        region="LT-Siauliai", plan="cloud_vps_1"
    )

    vps = facade.servers.create(creation_req, project.get_model().id)
    yield vps
    vps.delete()


@pytest.fixture(scope="package")
def baremetal_server(
    facade: cherryservers_sdk_python.facade.CherryApiFacade,
) -> cherryservers_sdk_python.servers.Server:
    """Retrieve a pre-built bare-metal server."""
    server_id = os.environ.get("CHERRY_TEST_BAREMETAL_SERVER_ID")
    assert server_id, "CHERRY_TEST_BAREMETAL_SERVER_ID environment variable is not set"

    return facade.servers.get_by_id(int(server_id))


@pytest.fixture(scope="package")
def sshkey(
    facade: cherryservers_sdk_python.facade.CherryApiFacade,
) -> Generator[cherryservers_sdk_python.sshkeys.SSHKey]:
    """Initialize a Cherry servers SSH key."""
    sshkey = facade.sshkeys.create(
        cherryservers_sdk_python.sshkeys.CreationRequest(
            label="python-sdk-server-test",
            key="ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBYe+GfesnLP06tfLOJWLFnGIJNpgrzLYE2VZhcmrFy0 example@gmail.com",
        )
    )

    yield sshkey
    sshkey.delete()
