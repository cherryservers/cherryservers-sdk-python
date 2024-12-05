"""Test cherryservers_sdk_python SSH key functionality."""

from __future__ import annotations

import pytest
import requests

import cherryservers_sdk_python


class TestSSHKey:
    """Test SSH key functionality."""

    @pytest.fixture(scope="class")
    def ssh_key(
        self, facade: cherryservers_sdk_python.facade.CherryApiFacade
    ) -> cherryservers_sdk_python.sshkeys.SSHKey:
        """Initialize a Cherry Servers SSH key."""
        creation_req = cherryservers_sdk_python.sshkeys.CreationRequest(
            key="ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBYe+GfesnLP06tfLOJWLFnGIJNpgrzLYE2VZhcmrFy8 example@gmail.com",
            label="cherryservers_sdk_python-python-sdk-test",
        )
        ssh_key = facade.sshkeys.create(creation_req)
        key_model = ssh_key.get_model()

        assert key_model.label == creation_req.label
        assert key_model.key == creation_req.key

        return ssh_key

    def test_get_by_id(
        self,
        ssh_key: cherryservers_sdk_python.sshkeys.SSHKey,
        facade: cherryservers_sdk_python.facade.CherryApiFacade,
    ) -> None:
        """Test getting a single SSH key by ID."""
        key_model = ssh_key.get_model()
        retrieved_key = facade.sshkeys.get_by_id(key_model.id)

        retrieved_model = retrieved_key.get_model()

        assert key_model.label == retrieved_model.label
        assert key_model.key == retrieved_model.key

    def test_get_all(
        self,
        ssh_key: cherryservers_sdk_python.sshkeys.SSHKey,
        facade: cherryservers_sdk_python.facade.CherryApiFacade,
    ) -> None:
        """Test getting all SSH keys."""
        keys = facade.sshkeys.get_all()

        retrieved_key_models = [key.get_model() for key in keys]
        fixture_key_model = ssh_key.get_model()

        assert any(
            key_model.label == fixture_key_model.label
            and key_model.key == fixture_key_model.key
            for key_model in retrieved_key_models
        )

    def test_update(self, ssh_key: cherryservers_sdk_python.sshkeys.SSHKey) -> None:
        """Test updating an SSH key."""
        update_req = cherryservers_sdk_python.sshkeys.UpdateRequest(
            label="cherryservers_sdk_python-python-sdk-test-updated",
            key="ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBYe+GfesnLP06tfLOJWLFnGIJNpgrzLYE2VZhcmrFy9 example@gmail.com",
        )
        ssh_key.update(update_req)

        updated_key_model = ssh_key.get_model()

        assert updated_key_model.label == update_req.label
        assert updated_key_model.key == update_req.key

    def test_delete(
        self,
        ssh_key: cherryservers_sdk_python.sshkeys.SSHKey,
        facade: cherryservers_sdk_python.facade.CherryApiFacade,
    ) -> None:
        """Test deleting an SSH key."""
        ssh_key.delete()

        key_model = ssh_key.get_model()

        with pytest.raises(requests.exceptions.HTTPError):
            facade.sshkeys.get_by_id(key_model.id)
