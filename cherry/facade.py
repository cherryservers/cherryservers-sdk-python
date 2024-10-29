"""Cherry Servers API Python facade."""

from __future__ import annotations

from cherry import _client, projects, regions, sshkeys, users


class CherryApiFacade:
    """Cherry Servers API Python facade.

    This is the preferred way of managing Cherry Servers resources with the SDK.
    For Cherry Servers API reference, see https://api.cherryservers.com/doc/.

    Attributes:
        users (users.UserClient): Manage user resources.
        sshkeys (sshkeys.SSHKeyClient): Manage SSH key resources.
        projects (projects.ProjectClient): Manage project resources.
        regions (regions.RegionClient): Manage region resources.

    """

    def __init__(self, token: str, user_agent_suffix: str = "") -> None:
        """Create a new :class:`CherryApiFacade` instance.

        :param str token: Cherry Servers API token. Can be created at https://portal.cherryservers.com/settings/api-keys.
        :param str user_agent_suffix:
         User-Agent suffix that will be added to the header. Empty by default.
        """
        self._api_client = _client.CherryApiClient(
            token=token, user_agent_suffix=user_agent_suffix
        )

        self.users = users.UserClient(self._api_client)

        self.sshkeys = sshkeys.SSHKeyClient(self._api_client)

        self.projects = projects.ProjectClient(self._api_client)

        self.regions = regions.RegionClient(self._api_client)
