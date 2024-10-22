"""TODO."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cherry.users.client import UserClient
    from cherry.users.model import UserModel


class User:
    """TODO."""

    def __init__(self, client: UserClient, model: UserModel) -> None:
        """TODO."""
        self._client = client
        self.model = model
