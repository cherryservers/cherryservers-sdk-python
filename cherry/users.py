"""Cherry Servers user resource management module."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import Field

from cherry import _models

if TYPE_CHECKING:
    from cherry import _client


class UserModel(_models.DefaultModel):
    """Cherry Servers user model.

    This model is frozen by default,
    since it represents an actual Cherry Servers user resource state.

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
    """Cherry Servers user resource.

    This class represents an existing Cherry Servers resource
    and should only be initialized by :class:`UserClient`.

    Attributes:
        model (UserModel): Cherry Servers user model.
            This is a Pydantic model that contains user data.
            A standard dictionary can be extracted with ``model.model_dump()``.

    """

    def __init__(self, client: UserClient, model: UserModel) -> None:
        """Initialize a Cherry Servers user resource."""
        self._client = client
        self.model = model


class UserClient:
    """Cherry Servers user client.

    Manage Cherry Servers user resources. This class should typically be initialized by
    :class:`cherry.facade.CherryApiFacade`.

    Example:
        .. code-block:: python

            facade = cherry.facade.CherryApiFacade(token="my-token")

            # Retrieve by ID.
            user = facade.users.get_by_id(123456)

            # Retrieve current user..
            user = facade.users.get_current_user()

    """

    def __init__(self, api_client: _client.CherryApiClient) -> None:
        """Initialize a Cherry Servers user client."""
        self._api_client = api_client

    def get_by_id(self, user_id: int) -> User:
        """Retrieve a user by ID."""
        response = self._api_client.get(f"users/{user_id}", None, 5)
        user_model = UserModel.model_validate(response.json())
        return User(self, user_model)

    def get_current_user(self) -> User:
        """Retrieve the current user."""
        response = self._api_client.get("user", None, 5)
        user_model = UserModel.model_validate(response.json())
        return User(self, user_model)
