"""TODO."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from cherry.users.user import User

if TYPE_CHECKING:
    from cherry._client import CherryApiClient
    from cherry.users.model import UserModel


class UserClient:
    """TODO."""

    def __init__(self, api_client: CherryApiClient) -> None:
        """TODO."""
        self._api_client = api_client

    def get_by_id(self, user_id: int, params: dict[str, Any] | None = None) -> User:
        """TODO."""
        r = self._api_client.get(f"users/{user_id}", params, 5)
        content = r.json()
        usr_model: UserModel = {
            "id": content["id"],
            "first_name": content["first_name"],
            "last_name": content["last_name"],
            "email": content["email"],
            "email_verified": content["email_verified"],
            "phone": content["phone"],
            "security_phone": content["security_phone"],
            "security_phone_verified": content["security_phone_verified"],
            "href": content["href"],
        }
        return User(self, usr_model)
