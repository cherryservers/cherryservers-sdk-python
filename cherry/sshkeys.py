"""Cherry Servers SSH key resource management module."""

from __future__ import annotations

from pydantic import Field

from cherry import _client, _models, users


class SSHKeyModel(_models.DefaultModel):
    """Cherry Servers SSH key model.

    This model is frozen by default,
    since it represents an actual Cherry Servers SSH key resource state.

    Attributes:
        id (int): SSH key ID.
        label (str): SSH key label.
        key (str): Public SSH key.
        fingerprint (str): SSH key fingerprint.
        user (cherry.users.UserModel): SSH key user.
        updated (str): Timestamp of the last SSH key update.
        created (str): Timestamp of the SSH key creation.
        href (str): SSH key href.

    """

    id: int = Field(description="SSH key ID.")
    label: str = Field(description="SSH key label.")
    key: str = Field(description="Public SSH key.")
    fingerprint: str = Field(description="SSH key fingerprint.")
    user: users.UserModel = Field(description="SSH key user.")
    updated: str = Field(description="Timestamp of the last SSH key update.")
    created: str = Field(description="Timestamp of the SSH key creation.")
    href: str = Field(description="SSH key href.")


class CreationRequest(_models.CherryRequestSchema):
    """Cherry Servers SSH key creation request schema.

    Attributes:
        label (str): SSH key label.
        key (str): Public SSH key.

    """

    label: str = Field(description="SSH key label.")
    key: str = Field(description="Public SSH key.")


class UpdateRequest(_models.CherryRequestSchema):
    """Cherry Servers SSH key update request schema.

    Attributes:
        label (str | None): SSH key label.
        key (str | None): Public SSH key.

    """

    label: str | None = Field(description="SSH key label.", default=None)
    key: str | None = Field(description="Public SSH key.", default=None)


class SSHKey:
    """Cherry Servers SSH key resource.

    This class represents an existing Cherry Servers resource
    and should only be initialized by :class:`SSHKeyClient`.

    Attributes:
        model (SSHKeyModel): Cherry Servers SSH key model.
            This is a Pydantic model that contains SSH key data.
            A standard dictionary can be extracted with ``model.model_dump()``.

    """

    def __init__(self, client: SSHKeyClient, model: SSHKeyModel) -> None:
        """Initialize a Cherry Servers SSH key resource."""
        self._client = client
        self.model = model

    def delete(self) -> None:
        """Delete Cherry Servers SSH key resource."""
        self._client.delete(self.model.id)

    def update(self, update_schema: UpdateRequest) -> None:
        """Update Cherry Servers SSH key resource."""
        updated = self._client.update(self.model.id, update_schema)
        self.model = updated.model


class SSHKeyClient:
    """Cherry Servers SSH key client.

    Manage Cherry Servers SSH key resources.
    This class should typically be initialized by
    :class:`cherry.facade.CherryApiFacade`.

    Example:
        .. code-block:: python

            # Create SSH key.
            facade = cherry.facade.CherryApiFacade(token="my-token")
            req = cherry.sshkeys.CreationRequest(
                label = "test",
                key = "my-public-api-key"
            )
            sshkey = facade.sshkeys.create(req)

            # Update SSH key.
            upd_req = cherry.sshkeys.UpdateRequest(
                label = "test-updated"
            )
            sshkey.update(upd_req)

            # Remove SSH key.
            sshkey.delete()

    """

    def __init__(self, api_client: _client.CherryApiClient) -> None:
        """Initialize a Cherry Servers SSH key client."""
        self._api_client = api_client

    def get_by_id(self, sshkey_id: int) -> SSHKey:
        """Retrieve a SSH key by ID."""
        response = self._api_client.get(
            f"ssh-keys/{sshkey_id}",
            {"fields": "ssh_key,user"},
            5,
        )
        sshkey_model = SSHKeyModel.model_validate(response.json())
        return SSHKey(self, sshkey_model)

    def get_all(self) -> list[SSHKey]:
        """Retrieve all SSH keys."""
        response = self._api_client.get("ssh-keys", {"fields": "ssh_key,user"}, 5)
        keys: list[SSHKey] = []
        for value in response.json():
            sshkey_model = SSHKeyModel.model_validate(value)
            keys.append(SSHKey(self, sshkey_model))

        return keys

    def create(self, creation_schema: CreationRequest) -> SSHKey:
        """Create a new SSH key."""
        response = self._api_client.post("ssh-keys", creation_schema, None, 5)
        return self.get_by_id(response.json()["id"])

    def delete(self, sshkey_id: int) -> None:
        """Delete SSH key by ID."""
        self._api_client.delete(f"ssh-keys/{sshkey_id}", None, 5)

    def update(self, sshkey_id: int, update_schema: UpdateRequest) -> SSHKey:
        """Update SSH key by ID."""
        response = self._api_client.put(f"ssh-keys/{sshkey_id}", update_schema, None, 5)
        return self.get_by_id(response.json()["id"])
