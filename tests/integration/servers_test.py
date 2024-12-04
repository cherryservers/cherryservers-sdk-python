"""Test cherry server functionality."""

from __future__ import annotations

import secrets
import string
from typing import TYPE_CHECKING

import pytest
import requests

import cherry

if TYPE_CHECKING:
    from collections.abc import Generator


def _generate_password(length: int) -> str:
    """Generate a random password.

    The password is guaranteed to:
        1. Be at least 8 characters long, but no longer than 24 characters.
        2. Have at least one lowercase letter.
        3. Have at least one uppercase letter, that is not the first character.
        4. Have at least one digit, that is not the last character.
        5. Not have any of ' " ` ! $ % & ; % #
    """
    length = max(8, length)
    length = min(24, length)

    lowercase = secrets.choice(string.ascii_lowercase)
    uppercase = secrets.choice(string.ascii_uppercase)
    digit = secrets.choice(string.digits)
    remaining = "".join(
        secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
        for _1 in range(length - 3)
    )
    return f"{lowercase}{uppercase}{digit}{remaining}"


class TestServer:
    """Test Server functionality."""

    @pytest.fixture(scope="class")
    def fip(
        self, facade: cherry.facade.CherryApiFacade, project: cherry.projects.Project
    ) -> Generator[cherry.ips.IP]:
        """Initialize a Cherry servers floating IP address."""
        fip = facade.ips.create(
            cherry.ips.CreationRequest(
                region="eu_nord_1",
            ),
            project.get_id(),
        )
        yield fip
        fip.update(cherry.ips.UpdateRequest(targeted_to=0))
        fip.delete()

    @pytest.fixture(scope="class")
    def server(
        self, facade: cherry.facade.CherryApiFacade, project: cherry.projects.Project
    ) -> cherry.servers.Server:
        """Initialize a Cherry Servers server."""
        creation_req = cherry.servers.CreationRequest(
            region="eu_nord_1",
            plan="cloud_vps_1",
        )
        server = facade.servers.create(creation_req, project.get_id())
        server_model = server.get_model()

        if server_model.region:
            assert server_model.region.slug == creation_req.region
        assert server_model.plan is not None
        assert server_model.plan.slug == creation_req.plan

        return server

    def test_create_with_full_params(
        self,
        facade: cherry.facade.CherryApiFacade,
        project: cherry.projects.Project,
        sshkey: cherry.sshkeys.SSHKey,
        fip: cherry.ips.IP,
    ) -> None:
        """Test creating a server with full params provided."""
        creation_req = cherry.servers.CreationRequest(
            region="eu_nord_1",
            plan="cloud_vps_1",
            image="debian_12_64bit",
            hostname="python-sdk-test",
            user_data="I2Nsb3VkLWNvbmZpZwp3cml0ZV9maWxlczoKICAt"
            "IHBhdGg6IC9oZWxsb193b3JsZC50eHQKICAgIGNvbnRlbnQ"
            "6IHwKICAgICAgSGVsbG8gV29ybGQKCnJ1bmNtZDoKICAt"
            "IGVjaG8gIkZpbGUgY3JlYXRlZCBzdWNjZXNzZnVsbHkhIgoK",
            ssh_keys={sshkey.get_model().id},
            ip_addresses={fip.get_id()},
            tags={"env": "test"},
        )

        server = facade.servers.create(creation_req, project.get_id())
        server_model = server.get_model()

        if server_model.region is not None:
            assert server_model.region.slug == creation_req.region
        assert server_model.plan is not None
        assert server_model.plan.slug == creation_req.plan
        if server_model.deployed_image is not None:
            assert server_model.deployed_image.slug == creation_req.image
        assert server_model.hostname == creation_req.hostname
        if server_model.ssh_keys is not None:
            assert server_model.ssh_keys[0].id == sshkey.get_model().id
        assert server_model.tags == creation_req.tags

        server.delete()

    def test_get_by_id(
        self, server: cherry.servers.Server, facade: cherry.facade.CherryApiFacade
    ) -> None:
        """Test getting a single server by ID."""
        server_model = server.get_model()
        retrieved_server = facade.servers.get_by_id(server_model.id)
        retrieved_server_model = retrieved_server.get_model()

        assert server_model.plan is not None
        assert retrieved_server_model.plan is not None
        assert server_model.plan.slug == retrieved_server_model.plan.slug
        if (
            server_model.region is not None
            and retrieved_server_model.region is not None
        ):
            assert server_model.region.slug == retrieved_server_model.region.slug

    def test_get_by_project(
        self,
        facade: cherry.facade.CherryApiFacade,
        project: cherry.projects.Project,
        server: cherry.servers.Server,
    ) -> None:
        """Test getting a list of server that belong to a project."""
        servers = facade.servers.get_by_project(project.get_id())

        retrieved_server_models = [
            retrieved_server.get_model() for retrieved_server in servers
        ]
        fixture_server_model = server.get_model()

        assert any(
            server_model.id == fixture_server_model.id
            for server_model in retrieved_server_models
        )

    def test_update(self, server: cherry.servers.Server) -> None:
        """Test updating a server."""
        update_req = cherry.servers.UpdateRequest(
            name="python-sdk-server-update-test",
            hostname="python-sdk-server-update-test",
            tags={"env": "test-upd"},
        )
        server.update(update_req)
        server_model = server.get_model()

        assert server_model.name == update_req.name
        assert server_model.tags == update_req.tags
        assert server_model.hostname == update_req.hostname

    def test_rescue_mode(self, baremetal_server: cherry.servers.Server) -> None:
        """Test server rescue mode."""
        baremetal_server.enter_rescue_mode(
            cherry.servers.EnterRescueModeRequest(password=_generate_password(16))
        )

        assert baremetal_server.get_status() == "rescue mode"

        baremetal_server.exit_rescue_mode()

        assert baremetal_server.get_status() == "deployed"

    def test_power_switch(self, baremetal_server: cherry.servers.Server) -> None:
        """Test server power switch."""
        baremetal_server.power_off()

        baremetal_server.power_on()

        # There is currently no way to check if the server is powered off.
        assert baremetal_server.get_status() == "deployed"

    def test_reboot(self, baremetal_server: cherry.servers.Server) -> None:
        """Test server reboot."""
        baremetal_server.reboot()

        assert baremetal_server.get_status() == "deployed"

    def test_rebuild(
        self, server: cherry.servers.Server, sshkey: cherry.sshkeys.SSHKey
    ) -> None:
        """Test server rebuild."""
        rebuild_req = cherry.servers.RebuildRequest(
            hostname="python-sdk-server-rebuild-test",
            image="debian_12_64bit",
            user_data="I2Nsb3VkLWNvbmZpZwp3cml0ZV9maWxlczoKICAt"
            "IHBhdGg6IC9oZWxsb193b3JsZC50eHQKICAgIGNvbnRlbnQ"
            "6IHwKICAgICAgSGVsbG8gV29ybGQKCnJ1bmNtZDoKICAt"
            "IGVjaG8gIkZpbGUgY3JlYXRlZCBzdWNjZXNzZnVsbHkhIgoK",
            ssh_keys={sshkey.get_model().id},
            password=_generate_password(16),
        )
        server.rebuild(rebuild_req)

        server_model = server.get_model()

        assert server_model.hostname == rebuild_req.hostname
        assert server_model.deployed_image is not None
        assert server_model.deployed_image.slug == rebuild_req.image
        assert server_model.ssh_keys is not None
        assert server_model.ssh_keys[0].id == sshkey.get_model().id

    def test_delete(
        self, server: cherry.servers.Server, facade: cherry.facade.CherryApiFacade
    ) -> None:
        """Test deleting a server."""
        server.delete()

        with pytest.raises(requests.exceptions.HTTPError):
            facade.servers.get_by_id(server.get_id())
