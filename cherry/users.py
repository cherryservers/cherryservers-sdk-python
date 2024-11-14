"""Cherry Servers user resource management module."""

from __future__ import annotations

from pydantic import Field

from cherry import _base


class UserModel(_base.ResourceModel):
    """Cherry Servers user model.

    This model is frozen by default,
    since it represents an actual Cherry Servers user resource state.

    Attributes:
        id (int): ID of the user.
        first_name (str | None): First name of the user.
        last_name (str | None): Last name of the user.
        email (str | None): Email address of the user.
        email_verified (bool | None): Whether user email address is verified.
        phone(str | None): Phone number of the user.
        security_phone(str | None): Security phone number of the user.
        security_phone_verified(bool | None):
        Whether user security phone number is verified.
        href(str | None): Href URL of the user.

    """

    id: int = Field(description="ID of the user.")
    first_name: str | None = Field(description="First name of the user.", default=None)
    last_name: str | None = Field(description="Last name of the user.", default=None)
    email: str | None = Field(description="Email address of the user.", default=None)
    email_verified: bool | None = Field(
        description="Whether user email address is verified.", default=None
    )
    phone: str | None = Field(description="Phone number of the user.", default=None)
    security_phone: str | None = Field(
        description="Security phone number of the user.", default=None
    )
    security_phone_verified: bool | None = Field(
        description="Whether user security phone number is verified.", default=None
    )
    href: str | None = Field(description="Href URL of the user.", default=None)


class UserClient(_base.ResourceClient):
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


class User(_base.Resource[UserClient, UserModel]):
    """Cherry Servers user resource.

    This class represents an existing Cherry Servers resource
    and should only be initialized by :class:`UserClient`.
    """
