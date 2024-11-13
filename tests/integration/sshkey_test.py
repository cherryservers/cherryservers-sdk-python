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

        assert ssh_key.model.label == creation_req.label
        assert ssh_key.model.key == creation_req.key

        return ssh_key

    def test_get_by_id(
        self, ssh_key: cherry.sshkeys.SSHKey, facade: cherry.facade.CherryApiFacade
    ) -> None:
        """Test getting a single SSH key by ID."""
        key = facade.sshkeys.get_by_id(ssh_key.model.id)

        assert key.model.label == ssh_key.model.label
        assert key.model.key == ssh_key.model.key

    def test_get_all(
        self, ssh_key: cherry.sshkeys.SSHKey, facade: cherry.facade.CherryApiFacade
    ) -> None:
        """Test getting all SSH keys."""
        keys = facade.sshkeys.get_all()

        assert any(
            key.model.label == ssh_key.model.label
            and key.model.key == ssh_key.model.key
            for key in keys
        )

    def test_update(self, ssh_key: cherry.sshkeys.SSHKey) -> None:
        """Test updating an SSH key."""
        update_req = cherry.sshkeys.UpdateRequest(
            label="cherry-python-sdk-test-updated",
            key="ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBYe+GfesnLP06tfLOJWLFnGIJNpgrzLYE2VZhcmrFy9 example@gmail.com",
        )
        ssh_key.update(update_req)

        assert ssh_key.model.label == update_req.label
        assert ssh_key.model.key == update_req.key

    def test_delete(
        self, ssh_key: cherry.sshkeys.SSHKey, facade: cherry.facade.CherryApiFacade
    ) -> None:
        """Test deleting an SSH key."""
        ssh_key.delete()

        with pytest.raises(requests.exceptions.HTTPError):
            facade.sshkeys.get_by_id(ssh_key.model.id)
