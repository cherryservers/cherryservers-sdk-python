from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import Field

from cherry import _models

if TYPE_CHECKING:
    from cherry import _client


class UserModel(_models.DefaultModel):
    """Cherry Servers User model.

    Attributes:
        id (int): ID of the user.
        first_name (str): First name of the user.
        last_name (str): Last name of the user.
        email (str): Email address of the user.
        email_verified (bool): Whether user email address is verified.
        phone(str): Phone number of the user.
        security_phone(str): Security phone number of the user.
        security_phone_verified(bool): Whether user security phone number is verified.
        href(str): Href URL of the user.

    """

    id: int = Field(description="ID of the user.")
    first_name: str = Field(description="First name of the user.")
    last_name: str = Field(description="Last name of the user.")
    email: str = Field(description="Email address of the user.")
    email_verified: bool = Field(description="Whether user email address is verified.")
    phone: str = Field(description="Phone number of the user.")
    security_phone: str = Field(description="Security phone number of the user.")
    security_phone_verified: bool = Field(
        description="Whether user security phone number is verified."
    )
    href: str = Field(description="Href URL of the user.")


class User:
    """Cherry Servers user.

    This class represents an existing Cherry Servers User resource and
    should only be instantiated by the UserClient.

    Attributes:
        model (UserModel): Cherry Servers User model.
            This is Pydantic model that contains user data.
            A standard dictionary can be extracted with model.model_dump().

    """

    def __init__(self, client: UserClient, model: UserModel) -> None:
        self._client = client
        self.model = model


class UserClient:
    """TODO."""

    def __init__(self, api_client: _client.CherryApiClient) -> None:
        """TODO."""
        self._api_client = api_client

    def get_by_id(self, user_id: int) -> User:
        """TODO."""
        response = self._api_client.get(f"users/{user_id}", None, 5)
        user_model = UserModel.model_validate(response.json())
        return User(self, user_model)

    def get_current_user(self) -> User:
        """TODO."""
        response = self._api_client.get("user", None, 5)
        user_model = UserModel.model_validate(response.json())
        return User(self, user_model)
