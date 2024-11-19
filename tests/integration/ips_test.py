"""Test cherry ips functionality."""

from __future__ import annotations

import pytest

import cherry


class TestIP:
    """Test IP functionality."""

    @pytest.fixture(scope="class")
    def ip(
        self, facade: cherry.facade.CherryApiFacade, project: cherry.projects.Project
    ) -> cherry.ips.IP:
        """Initialize a Cherry Servers IP."""
        creation_req = cherry.ips.CreationRequest(region="eu_nord_1")
        return facade.ips.create(creation_req, project.get_model_copy().id)

    def test_create_full_params(
        self,
        vps: cherry.servers.Server,
        project: cherry.projects.Project,
        facade: cherry.facade.CherryApiFacade,
    ) -> None:
        """Test IP creation with all optional parameters."""
        vps_model = vps.get_model_copy()
        creation_req = cherry.ips.CreationRequest(
            region="eu_nord_1",
            targeted_to=vps_model.id,
            ptr_record="python-sdk-test",
            a_record="python-sdk-test",
            ddos_scrubbing=False,
            tags={"env": "test"},
        )

        ip = facade.ips.create(creation_req, project.get_model_copy().id)
        ip_model = ip.get_model_copy()

        if ip_model.region is not None:
            assert ip_model.region.slug == "eu_nord_1"
        if ip_model.targeted_to is not None:
            assert ip_model.targeted_to.id == vps_model.id
        assert ip_model.ptr_record == "python-sdk-test."
        assert ip_model.a_record == "python-sdk-test.cloud.cherryservers.net."
        assert ip_model.ddos_scrubbing is False
        assert ip_model.tags == {"env": "test"}

        detach_req = cherry.ips.UpdateRequest(targeted_to=0)
        ip.update(detach_req)
        ip.delete()

    def test_get_by_id(
        self, ip: cherry.ips.IP, facade: cherry.facade.CherryApiFacade
    ) -> None:
        """Test getting a single IP by ID."""
        ip_model = ip.get_model_copy()
        retrieved_ip = facade.ips.get_by_id(ip_model.id)

        retrieved_model = retrieved_ip.get_model_copy()

        assert ip_model.id == retrieved_model.id
        assert ip_model.address == retrieved_model.address

    def test_get_by_project(
        self,
        project: cherry.projects.Project,
        facade: cherry.facade.CherryApiFacade,
        ip: cherry.ips.IP,
    ) -> None:
        """Test getting IPs by project."""
        ips = facade.ips.get_by_project(project.get_model_copy().id)

        retrieved_ip_models = [ip.get_model_copy() for ip in ips]
        fixture_ip_model = ip.get_model_copy()

        assert any(
            ip_model.id == fixture_ip_model.id
            and ip_model.address == fixture_ip_model.address
            for ip_model in retrieved_ip_models
        )

    def test_update(self, ip: cherry.ips.IP, vps: cherry.servers.Server) -> None:
        """Test updating an IP."""
        vps_model = vps.get_model_copy()
        vps_public_ip_id = None
        assert vps_model.ip_addresses is not None, "no IPs assigned to VPS fixture."
        for vps_ip in vps_model.ip_addresses:
            if vps_ip.type == "primary-ip":
                vps_public_ip_id = vps_ip.id
                break

        assert vps_public_ip_id is not None, "no public IP found for VPS fixture."

        update_req = cherry.ips.UpdateRequest(
            ptr_record="python-sdk-test-upd",
            a_record="python-sdk-test-upd",
            routed_to=vps_public_ip_id,
            tags={"env": "test-upd"},
        )

        ip.update(update_req)

        updated_ip_model = ip.get_model_copy()

        assert updated_ip_model.ptr_record == "python-sdk-test-upd."
        assert (
            updated_ip_model.a_record == "python-sdk-test-upd.cloud.cherryservers.net."
        )
        if updated_ip_model.routed_to is not None:
            assert updated_ip_model.routed_to.id == vps_public_ip_id
        assert updated_ip_model.tags == {"env": "test-upd"}

    def test_delete(self, ip: cherry.ips.IP) -> None:
        """Test deleting an IP."""
        with pytest.raises(cherry.ips.AddressAttachedError):
            ip.delete()

        ip.update(cherry.ips.UpdateRequest(targeted_to=0))
        ip.delete()

        # IPs aren't deleted immediately, so we can't check if deletion succeeded
        # by checking if trying to get_by_id produces an error.
