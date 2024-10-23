from __future__ import annotations

from pydantic import Field

from cherry import _client, _models, _users, request_schemas


class SSHKeyModel(_models.DefaultModel):
    """Cherry Servers SSH key model.

    Attributes:
        id (int): SSH key ID.
        label (str): SSH key label.
        key (str): Public SSH key.
        fingerprint (str): SSH key fingerprint.
        user (cherry._users.UserModel): SSH key user.
        updated (str): Timestamp of the last SSH key update.
        created (str): Timestamp of the SSH key creation.
        href (str): SSH key href.

    """

    id: int = Field(description="SSH key ID.")
    label: str = Field(description="SSH key label.")
    key: str = Field(description="Public SSH key.")
    fingerprint: str = Field(description="SSH key fingerprint.")
    user: _users.UserModel = Field(description="SSH key user.")
    updated: str = Field(description="Timestamp of the last SSH key update.")
    created: str = Field(description="Timestamp of the SSH key creation.")
    href: str = Field(description="SSH key href.")


class SSHKey:
    """TODO."""

    def __init__(self, client: SSHKeyClient, model: SSHKeyModel) -> None:
        """TODO."""
        self._client = client
        self.model = model

    def delete(self) -> None:
        """TODO."""
        self._client.delete(self.model.id)

    def update(self, update_schema: request_schemas.sshkeys.Update) -> SSHKey:
        """TODO."""
        return self._client.update(self.model.id, update_schema)


class SSHKeyClient:
    """TODO."""

    def __init__(self, api_client: _client.CherryApiClient) -> None:
        """TODO."""
        self._api_client = api_client

    def get_by_id(self, sshkey_id: int) -> SSHKey:
        """TODO."""
        response = self._api_client.get(
            f"ssh-keys/{sshkey_id}",
            {"fields": "ssh_key,user"},
            5,
        )
        sshkey_model = SSHKeyModel.model_validate(response.json())
        return SSHKey(self, sshkey_model)

    def list(self) -> list[SSHKey]:
        """TODO."""
        response = self._api_client.get("ssh-keys", {"fields": "ssh_key,user"}, 5)
        keys: list[SSHKey] = []
        for value in response.json():
            sshkey_model = SSHKeyModel.model_validate(value)
            keys.append(SSHKey(self, sshkey_model))

        return keys

    def create(self, creation_schema: request_schemas.sshkeys.Creation) -> SSHKey:
        """TODO."""
        response = self._api_client.post("ssh-keys", creation_schema, None, 5)
        return self.get_by_id(response.json()["id"])

    def delete(self, sshkey_id: int) -> None:
        """TODO."""
        self._api_client.delete(f"ssh-keys/{sshkey_id}", None, 5)

    def update(
        self, sshkey_id: int, update_schema: request_schemas.sshkeys.Update
    ) -> SSHKey:
        """TODO."""
        response = self._api_client.put(f"ssh-keys/{sshkey_id}", update_schema, None, 5)
        return self.get_by_id(response.json()["id"])
