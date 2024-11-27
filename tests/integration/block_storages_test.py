"""Test cherry block_storages functionality."""

from __future__ import annotations

import os

import pytest
import requests

import cherry


class TestBlockStorage:
    """Test Block Storage functionality."""

    @pytest.fixture(scope="class")
    def baremetal_server(
        self, facade: cherry.facade.CherryApiFacade
    ) -> cherry.servers.Server:
        """Retrieve a pre-built bare-metal server."""
        server_id = os.environ.get("CHERRY_TEST_BAREMETAL_SERVER_ID")
        assert (
            server_id
        ), "CHERRY_TEST_BAREMETAL_SERVER_ID environment variable is not set"

        return facade.servers.get_by_id(int(server_id))

    @pytest.fixture(scope="class")
    def project_id(self, baremetal_server: cherry.servers.Server) -> int:
        """Baremetal server project ID."""
        baremetal_server_model = baremetal_server.get_model_copy()
        assert baremetal_server_model.project is not None

        return baremetal_server_model.project.id

    @pytest.fixture(scope="class")
    def storage(
        self, facade: cherry.facade.CherryApiFacade, project_id: int
    ) -> cherry.block_storages.BlockStorage:
        """Initialize a Block Storage instance."""
        creation_req = cherry.block_storages.CreationRequest(region="eu_nord_1", size=1)

        return facade.block_storages.create(creation_req, project_id=project_id)

    def test_get_by_id(
        self,
        storage: cherry.block_storages.BlockStorage,
        facade: cherry.facade.CherryApiFacade,
    ) -> None:
        """Test getting a single block storage volume by ID."""
        storage_model = storage.get_model_copy()
        retrieved_storage = facade.block_storages.get_by_id(storage_model.id)

        retrieved_model = retrieved_storage.get_model_copy()

        assert storage_model.id == retrieved_model.id
        assert storage_model.name == retrieved_model.name

    def test_list_by_project(
        self,
        project_id: int,
        facade: cherry.facade.CherryApiFacade,
        storage: cherry.block_storages.BlockStorage,
    ) -> None:
        """Test listing block storage volumes by project."""
        storages = facade.block_storages.list_by_project(project_id)

        retrieved_storage_models = [storage.get_model_copy() for storage in storages]
        fixture_storage_model = storage.get_model_copy()

        assert any(
            storage_model.id == fixture_storage_model.id
            and storage_model.name == fixture_storage_model.name
            for storage_model in retrieved_storage_models
        )

    def test_attachment(
        self,
        storage: cherry.block_storages.BlockStorage,
        baremetal_server: cherry.servers.Server,
    ) -> None:
        """Test storage volume attachment to server.."""
        server_model = baremetal_server.get_model_copy()

        storage.attach(cherry.block_storages.AttachRequest(attach_to=server_model.id))
        storage_model = storage.get_model_copy()

        assert storage_model.attached_to is not None
        assert storage_model.attached_to.id == server_model.id

        storage.detach()

        assert storage.get_model_copy().attached_to is None

    def test_resize(
        self,
        storage: cherry.block_storages.BlockStorage,
    ) -> None:
        """Test storage volume resizing."""
        updated_size = 2
        storage.update(cherry.block_storages.UpdateRequest(size=updated_size))

        assert storage.get_model_copy().size == updated_size

    def test_delete(
        self,
        storage: cherry.block_storages.BlockStorage,
        facade: cherry.facade.CherryApiFacade,
    ) -> None:
        """Test deleting a block storage volume."""
        storage.delete()

        with pytest.raises(requests.exceptions.HTTPError):
            facade.block_storages.get_by_id(storage.get_model_copy().id)
