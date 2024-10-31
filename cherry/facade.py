"""Cherry Servers API Python facade."""

from __future__ import annotations

from cherry import _client, images, ips, plans, projects, regions, sshkeys, teams, users


class CherryApiFacade:
    """Cherry Servers API Python facade.

    This is the preferred way of managing Cherry Servers resources with the SDK.
    For Cherry Servers API reference, see https://api.cherryservers.com/doc/.

    Attributes:
        users (users.UserClient): Manage user resources.
        sshkeys (sshkeys.SSHKeyClient): Manage SSH key resources.
        projects (projects.ProjectClient): Manage project resources.
        regions (regions.RegionClient): Manage region resources.
        ips (ips.IPClient): Manage IP resources.
        teams (teams.TeamClient): Manage team resources.
        plans (plans.PlanClient): Manage plan resources.
        images (images.ImageClient): Manage image resources.

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

        self.ips = ips.IPClient(self._api_client)

        self.teams = teams.TeamClient(self._api_client)

        self.plans = plans.PlanClient(self._api_client)

        self.images = images.ImageClient(self._api_client)
