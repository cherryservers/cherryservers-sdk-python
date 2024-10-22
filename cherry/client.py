"""Cherry Servers API Python client."""

from __future__ import annotations

from ._client import CherryApiClient
from .users.client import UserClient


class Client:
    """Cherry Servers API Python client.

    For Cherry Servers API reference, see https://api.cherryservers.com/doc/.
    """

    def __init__(self, token: str, user_agent_suffix: str = "") -> None:
        """Create a new Client instance.

        :param token: Cherry Servers API token. Can be created at https://portal.cherryservers.com/settings/api-keys.
        :param user_agent_suffix: User-Agent suffix to add to the client headers.
        """
        self._api_client = CherryApiClient(
            token=token, user_agent_suffix=user_agent_suffix
        )

        self.users = UserClient(self._api_client)
