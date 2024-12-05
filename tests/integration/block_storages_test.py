"""Test cherryservers_sdk_python block_storages functionality."""

from __future__ import annotations

import pytest
import requests

import cherryservers_sdk_python


class TestBlockStorage:
    """Test Block Storage functionality."""

    @pytest.fixture(scope="class")
    def project_id(
        self, baremetal_server: cherryservers_sdk_python.servers.Server
    ) -> int:
        """Baremetal server project ID."""
        baremetal_server_model = baremetal_server.get_model()
        assert baremetal_server_model.project is not None

        return baremetal_server_model.project.id

    @pytest.fixture(scope="class")
    def storage(
        self, facade: cherryservers_sdk_python.facade.CherryApiFacade, project_id: int
    ) -> cherryservers_sdk_python.block_storages.BlockStorage:
        """Initialize a Block Storage instance."""
        creation_req = cherryservers_sdk_python.block_storages.CreationRequest(
            region="eu_nord_1", size=1
        )

        return facade.block_storages.create(creation_req, project_id=project_id)

    def test_get_by_id(
        self,
        storage: cherryservers_sdk_python.block_storages.BlockStorage,
        facade: cherryservers_sdk_python.facade.CherryApiFacade,
    ) -> None:
        """Test getting a single block storage volume by ID."""
        storage_model = storage.get_model()
        retrieved_storage = facade.block_storages.get_by_id(storage_model.id)

        retrieved_model = retrieved_storage.get_model()

        assert storage_model.id == retrieved_model.id
        assert storage_model.name == retrieved_model.name

    def test_list_by_project(
        self,
        project_id: int,
        facade: cherryservers_sdk_python.facade.CherryApiFacade,
        storage: cherryservers_sdk_python.block_storages.BlockStorage,
    ) -> None:
        """Test listing block storage volumes by project."""
        storages = facade.block_storages.list_by_project(project_id)

        retrieved_storage_models = [storage.get_model() for storage in storages]
        fixture_storage_model = storage.get_model()

        assert any(
            storage_model.id == fixture_storage_model.id
            and storage_model.name == fixture_storage_model.name
            for storage_model in retrieved_storage_models
        )

    def test_attachment(
        self,
        storage: cherryservers_sdk_python.block_storages.BlockStorage,
        baremetal_server: cherryservers_sdk_python.servers.Server,
    ) -> None:
        """Test storage volume attachment to server.."""
        server_model = baremetal_server.get_model()

        storage.attach(
            cherryservers_sdk_python.block_storages.AttachRequest(
                attach_to=server_model.id
            )
        )
        storage_model = storage.get_model()

        assert storage_model.attached_to is not None
        assert storage_model.attached_to.id == server_model.id

        storage.detach()

        assert storage.get_model().attached_to is None

    def test_resize(
        self,
        storage: cherryservers_sdk_python.block_storages.BlockStorage,
    ) -> None:
        """Test storage volume resizing."""
        updated_size = 2
        storage.update(
            cherryservers_sdk_python.block_storages.UpdateRequest(size=updated_size)
        )

        assert storage.get_model().size == updated_size

    def test_delete(
        self,
        storage: cherryservers_sdk_python.block_storages.BlockStorage,
        facade: cherryservers_sdk_python.facade.CherryApiFacade,
    ) -> None:
        """Test deleting a block storage volume."""
        storage.delete()

        with pytest.raises(requests.exceptions.HTTPError):
            facade.block_storages.get_by_id(storage.get_model().id)
