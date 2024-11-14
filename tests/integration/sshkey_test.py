"""Test cherry SSH key functionality."""

from __future__ import annotations

import pytest
import requests

import cherry


class TestSSHKey:
    """Test SSH key functionality."""

    @pytest.fixture(scope="class")
    def ssh_key(self, facade: cherry.facade.CherryApiFacade) -> cherry.sshkeys.SSHKey:
        """Initialize a Cherry Servers SSH key."""
        creation_req = cherry.sshkeys.CreationRequest(
            key="ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBYe+GfesnLP06tfLOJWLFnGIJNpgrzLYE2VZhcmrFy8 example@gmail.com",
            label="cherry-python-sdk-test",
        )
        ssh_key = facade.sshkeys.create(creation_req)
        key_model = ssh_key.get_model_copy()

        assert key_model.label == creation_req.label
        assert key_model.key == creation_req.key

        return ssh_key

    def test_get_by_id(
        self, ssh_key: cherry.sshkeys.SSHKey, facade: cherry.facade.CherryApiFacade
    ) -> None:
        """Test getting a single SSH key by ID."""
        key_model = ssh_key.get_model_copy()
        retrieved_key = facade.sshkeys.get_by_id(key_model.id)

        retrieved_model = retrieved_key.get_model_copy()

        assert key_model.label == retrieved_model.label
        assert key_model.key == retrieved_model.key

    def test_get_all(
        self, ssh_key: cherry.sshkeys.SSHKey, facade: cherry.facade.CherryApiFacade
    ) -> None:
        """Test getting all SSH keys."""
        keys = facade.sshkeys.get_all()

        retrieved_key_models = [key.get_model_copy() for key in keys]
        fixture_key_model = ssh_key.get_model_copy()

        assert any(
            key_model.label == fixture_key_model.label
            and key_model.key == fixture_key_model.key
            for key_model in retrieved_key_models
        )

    def test_update(self, ssh_key: cherry.sshkeys.SSHKey) -> None:
        """Test updating an SSH key."""
        update_req = cherry.sshkeys.UpdateRequest(
            label="cherry-python-sdk-test-updated",
            key="ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBYe+GfesnLP06tfLOJWLFnGIJNpgrzLYE2VZhcmrFy9 example@gmail.com",
        )
        ssh_key.update(update_req)

        updated_key_model = ssh_key.get_model_copy()

        assert updated_key_model.label == update_req.label
        assert updated_key_model.key == update_req.key

    def test_delete(
        self, ssh_key: cherry.sshkeys.SSHKey, facade: cherry.facade.CherryApiFacade
    ) -> None:
        """Test deleting an SSH key."""
        ssh_key.delete()

        key_model = ssh_key.get_model_copy()

        with pytest.raises(requests.exceptions.HTTPError):
            facade.sshkeys.get_by_id(key_model.id)
