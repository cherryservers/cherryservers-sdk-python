"""Integration test configuration."""

from __future__ import annotations

import os
import time
from typing import TYPE_CHECKING

import pytest

import cherry

if TYPE_CHECKING:
    from collections.abc import Generator


@pytest.fixture(scope="package")
def facade() -> cherry.facade.CherryApiFacade:
    """Initialize Cherry API facade."""
    token = os.environ.get("CHERRY_TEST_API_KEY")
    assert token, "CHERRY_TEST_API_KEY environment variable is not set"
    return cherry.facade.CherryApiFacade(token=token, user_agent_prefix="test")


@pytest.fixture(scope="package")
def team_id() -> int:
    """Get a pre-initialized Cherry Servers team."""
    team_id = os.environ.get("CHERRY_TEST_TEAM_ID")
    assert team_id, "CHERRY_TEST_TEAM_ID environment variable is not set"
    return int(team_id)


@pytest.fixture(scope="package")
def project(
    team_id: int, facade: cherry.facade.CherryApiFacade
) -> Generator[cherry.projects.Project]:
    """Initialize a Cherry Servers project."""
    creation_req = cherry.projects.CreationRequest(
        name="cherry-python-sdk-project-fixture"
    )
    project = facade.projects.create(creation_req, team_id=team_id)
    yield project
    project.delete()


@pytest.fixture(scope="package")
def vps(
    facade: cherry.facade.CherryApiFacade, project: cherry.projects.Project
) -> Generator[cherry.servers.Server]:
    """Initialize a Cherry Servers VPS."""
    creation_req = cherry.servers.CreationRequest(
        region="eu_nord_1", plan="cloud_vps_1"
    )

    vps = facade.servers.create(creation_req, project.get_model_copy().id)
    while vps.get_model_copy().state != "active":
        time.sleep(10)
        vps = facade.servers.get_by_id(vps.get_model_copy().id)
    yield vps
    vps.delete()


@pytest.fixture(scope="package")
def baremetal_server(facade: cherry.facade.CherryApiFacade) -> cherry.servers.Server:
    """Retrieve a pre-built bare-metal server."""
    server_id = os.environ.get("CHERRY_TEST_BAREMETAL_SERVER_ID")
    assert server_id, "CHERRY_TEST_BAREMETAL_SERVER_ID environment variable is not set"

    return facade.servers.get_by_id(int(server_id))


@pytest.fixture(scope="package")
def sshkey(facade: cherry.facade.CherryApiFacade) -> Generator[cherry.sshkeys.SSHKey]:
    """Initialize a Cherry servers SSH key."""
    sshkey = facade.sshkeys.create(
        cherry.sshkeys.CreationRequest(
            label="python-sdk-server-test",
            key="ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBYe+GfesnLP06tfLOJWLFnGIJNpgrzLYE2VZhcmrFy0 example@gmail.com",
        )
    )

    yield sshkey
    sshkey.delete()
