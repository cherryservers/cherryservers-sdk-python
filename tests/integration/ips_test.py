"""Test cherryservers_sdk_python ips functionality."""

from __future__ import annotations

import pytest

import cherryservers_sdk_python


class TestIP:
    """Test IP functionality."""

    @pytest.fixture(scope="class")
    def ip(
        self,
        facade: cherryservers_sdk_python.facade.CherryApiFacade,
        project: cherryservers_sdk_python.projects.Project,
    ) -> cherryservers_sdk_python.ips.IP:
        """Initialize a Cherry Servers IP."""
        creation_req = cherryservers_sdk_python.ips.CreationRequest(
            region="LT-Siauliai"
        )
        return facade.ips.create(creation_req, project.get_model().id)

    def test_create_full_params(
        self,
        vps: cherryservers_sdk_python.servers.Server,
        project: cherryservers_sdk_python.projects.Project,
        facade: cherryservers_sdk_python.facade.CherryApiFacade,
    ) -> None:
        """Test IP creation with all optional parameters."""
        vps_model = vps.get_model()
        creation_req = cherryservers_sdk_python.ips.CreationRequest(
            region="LT-Siauliai",
            targeted_to=vps_model.id,
            ptr_record="python-sdk-test",
            a_record="python-sdk-test",
            tags={"env": "test"},
        )

        ip = facade.ips.create(creation_req, project.get_model().id)
        ip_model = ip.get_model()

        if ip_model.region is not None:
            assert ip_model.region.slug == "LT-Siauliai"
        if ip_model.targeted_to is not None:
            assert ip_model.targeted_to.id == vps_model.id
        assert ip_model.ptr_record == "python-sdk-test."
        assert ip_model.a_record == "python-sdk-test.cloud.cherryservers.net."
        assert ip_model.tags == {"env": "test"}

        detach_req = cherryservers_sdk_python.ips.UpdateRequest(targeted_to=0)
        ip.update(detach_req)
        ip.delete()

    def test_get_by_id(
        self,
        ip: cherryservers_sdk_python.ips.IP,
        facade: cherryservers_sdk_python.facade.CherryApiFacade,
    ) -> None:
        """Test getting a single IP by ID."""
        ip_model = ip.get_model()
        retrieved_ip = facade.ips.get_by_id(ip_model.id)

        retrieved_model = retrieved_ip.get_model()

        assert ip_model.id == retrieved_model.id
        assert ip_model.address == retrieved_model.address

    def test_get_by_project(
        self,
        project: cherryservers_sdk_python.projects.Project,
        facade: cherryservers_sdk_python.facade.CherryApiFacade,
        ip: cherryservers_sdk_python.ips.IP,
    ) -> None:
        """Test getting IPs by project."""
        ips = facade.ips.list_by_project(project.get_model().id)

        retrieved_ip_models = [ip.get_model() for ip in ips]
        fixture_ip_model = ip.get_model()

        assert any(
            ip_model.id == fixture_ip_model.id
            and ip_model.address == fixture_ip_model.address
            for ip_model in retrieved_ip_models
        )

    def test_update(
        self,
        ip: cherryservers_sdk_python.ips.IP,
        vps: cherryservers_sdk_python.servers.Server,
    ) -> None:
        """Test updating an IP."""
        vps_model = vps.get_model()
        vps_public_ip_id = None
        assert vps_model.ip_addresses is not None, "no IPs assigned to VPS fixture."
        for vps_ip in vps_model.ip_addresses:
            if vps_ip.type == "primary-ip":
                vps_public_ip_id = vps_ip.id
                break

        assert vps_public_ip_id is not None, "no public IP found for VPS fixture."

        update_req = cherryservers_sdk_python.ips.UpdateRequest(
            ptr_record="python-sdk-test-upd",
            a_record="python-sdk-test-upd",
            routed_to=vps_public_ip_id,
            tags={"env": "test-upd"},
        )

        ip.update(update_req)

        updated_ip_model = ip.get_model()

        assert updated_ip_model.ptr_record == "python-sdk-test-upd."
        assert (
            updated_ip_model.a_record == "python-sdk-test-upd.cloud.cherryservers.net."
        )
        if updated_ip_model.routed_to is not None:
            assert updated_ip_model.routed_to.id == vps_public_ip_id
        assert updated_ip_model.tags == {"env": "test-upd"}

    def test_delete(self, ip: cherryservers_sdk_python.ips.IP) -> None:
        """Test deleting an IP."""
        with pytest.raises(cherryservers_sdk_python.ips.AddressAttachedError):
            ip.delete()

        ip.update(cherryservers_sdk_python.ips.UpdateRequest(targeted_to=0))
        ip.delete()

        # IPs aren't deleted immediately, so we can't check if deletion succeeded
        # by checking if trying to get_by_id produces an error.
