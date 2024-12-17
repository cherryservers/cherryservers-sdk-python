"""Unit tests for Cherry Servers Python SDK SSH keys client."""

from __future__ import annotations

from typing import TYPE_CHECKING
from unittest import mock

import pytest

import cherryservers_sdk_python.users
from tests.unit import resource_client_helpers, resource_helpers

if TYPE_CHECKING:
    import requests


class TestClient:
    """Test SSH key client."""

    @pytest.fixture
    def sshkeys_client(self) -> cherryservers_sdk_python.sshkeys.SSHKeyClient:
        """Initialize SSH key client fixture."""
        return cherryservers_sdk_python.sshkeys.SSHKeyClient(
            api_client=mock.MagicMock()
        )

    def test_get_by_id_success(
        self,
        get_sshkey_response: requests.Response,
        sshkeys_client: cherryservers_sdk_python.sshkeys.SSHKeyClient,
    ) -> None:
        """Test successfully getting SSH key by ID."""
        resource_client_helpers.check_getter_function(
            get_sshkey_response,
            sshkeys_client,
            lambda: sshkeys_client.get_by_id(1234),
        )

    def test_get_all_success(
        self,
        list_sshkeys_response: requests.Response,
        sshkeys_client: cherryservers_sdk_python.sshkeys.SSHKeyClient,
    ) -> None:
        """Test successfully getting all SSH keys."""
        resource_client_helpers.check_listing_function(
            list_sshkeys_response,
            sshkeys_client,
            sshkeys_client.get_all,
        )

    def test_create_success(
        self,
        post_sshkey_response: requests.Response,
        get_sshkey_response: requests.Response,
        sshkeys_client: cherryservers_sdk_python.sshkeys.SSHKeyClient,
    ) -> None:
        """Test successfully creating an SSH key."""
        creation_resp_json = post_sshkey_response.json()
        resource_client_helpers.check_creation_function(
            post_sshkey_response,
            get_sshkey_response,
            sshkeys_client,
            lambda: sshkeys_client.create(
                cherryservers_sdk_python.sshkeys.CreationRequest(
                    label=creation_resp_json["label"],
                    key=creation_resp_json["key"],
                )
            ),
        )

    def test_update_success(
        self,
        put_sshkey_response: requests.Response,
        get_sshkey_response: requests.Response,
        sshkeys_client: cherryservers_sdk_python.sshkeys.SSHKeyClient,
    ) -> None:
        """Test successfully updating an SSH key."""
        update_resp_json = put_sshkey_response.json()
        resource_client_helpers.check_update_function(
            put_sshkey_response,
            get_sshkey_response,
            sshkeys_client,
            lambda: sshkeys_client.update(
                1234,
                cherryservers_sdk_python.sshkeys.UpdateRequest(
                    label=update_resp_json["label"], key=update_resp_json["key"]
                ),
            ),
        )


class TestSSHKey:
    """Test SSH key resource."""

    @pytest.fixture
    def sshkey(
        self, get_sshkey_response: requests.Response
    ) -> cherryservers_sdk_python.sshkeys.SSHKey:
        """Initialize SSH key fixture."""
        return cherryservers_sdk_python.sshkeys.SSHKey(
            client=cherryservers_sdk_python.sshkeys.SSHKeyClient(
                api_client=mock.MagicMock()
            ),
            model=cherryservers_sdk_python.sshkeys.SSHKeyModel.model_validate(
                get_sshkey_response.json()
            ),
        )

    def test_get_id(
        self,
        sshkey: cherryservers_sdk_python.sshkeys.SSHKey,
        get_sshkey_response: requests.Response,
    ) -> None:
        """Test getting SSH key ID."""
        assert sshkey.get_id() == get_sshkey_response.json()["id"]

    def test_update(
        self,
        sshkey: cherryservers_sdk_python.sshkeys.SSHKey,
        put_sshkey_response: requests.Response,
        get_sshkey_after_update_response: requests.Response,
    ) -> None:
        """Test updating an SSH key."""
        update_resp_json = put_sshkey_response.json()
        resource_helpers.check_update_function(
            put_sshkey_response,
            get_sshkey_after_update_response,
            sshkey,
            lambda: sshkey.update(
                cherryservers_sdk_python.sshkeys.UpdateRequest(
                    label=update_resp_json["label"],
                    key=update_resp_json["key"],
                )
            ),
        )
