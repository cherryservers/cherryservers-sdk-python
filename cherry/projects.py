"""Cherry Servers project resource management module."""

from __future__ import annotations

from pydantic import Field

from cherry import _client, _models, request_schemas


class ProjectBGPModel(_models.DefaultModel):
    """Cherry Servers project BGP model.

    This model is frozen by default,
    since it represents an actual Cherry Servers project BGP resource state.

    Attributes:
        enabled (bool): Whether BGP is enabled for the project.
        local_asn (int): Local ASN of the project.

    """

    enabled: bool = Field(description="Whether BGP is enabled for the project.")
    local_asn: int = Field(description="Local ASN of the project.")


class ProjectModel(_models.DefaultModel):
    """Cherry Servers project model.

    This model is frozen by default,
    since it represents an actual Cherry Servers project resource state.

    Attributes:
        id (int): Project ID.
        name (str): Project name.
        bgp (cherry.projects.ProjectBGPModel): Project BGP.
        href (str): Project href.

    """

    id: int = Field(description="Project ID.")
    name: str = Field(description="Project name.")
    bgp: ProjectBGPModel = Field(description="Project BGP.")
    href: str = Field(description="Project href.")


class Project:
    """Cherry Servers project resource.

    This class represents an existing Cherry Servers resource
    and should only be initialized by :class:`ProjectClient`.

    Attributes:
        model (ProjectModel): Cherry Servers project model.
            This is a Pydantic model that contains project data.
            A standard dictionary can be extracted with ``model.model_dump()``.

    """

    def __init__(self, client: ProjectClient, model: ProjectModel) -> None:
        """Initialize a Cherry Servers project resource."""
        self._client = client
        self.model = model

    def delete(self) -> None:
        """Delete Cherry Servers project resource."""
        self._client.delete(self.model.id)

    def update(self, update_schema: request_schemas.projects.UpdateRequest) -> None:
        """Update Cherry Servers project resource."""
        updated = self._client.update(self.model.id, update_schema)
        self.model = updated.model


class ProjectClient:
    """Cherry Servers project client.

    Manage Cherry Servers project resources.
    This class should typically be initialized by
    :class:`cherry.facade.CherryApiFacade`.

    Example:
        .. code-block:: python

            facade = cherry.facade.CherryApiFacade(token="my-token")

            # Retrieve a project.
            existing_project = facade.projects.get_by_id(123456)

            # Create project.
            req = cherry.request_schemas.projects.CreationRequest(
                name = "my-project"
            )
            project = facade.projects.create(req, 123456)

            # Update project.
            upd_req = cherry.request_schemas.projects.UpdateRequest(
                name = "my-project-updated",
                bgp = True
            )
            project.update(upd_req)

            # Remove project.
            project.delete()

    """

    def __init__(self, api_client: _client.CherryApiClient) -> None:
        """Initialize a Cherry Servers project client."""
        self._api_client = api_client

    def get_by_id(self, project_id: int) -> Project:
        """Retrieve a project by ID."""
        response = self._api_client.get(
            f"projects/{project_id}",
            None,
            5,
        )
        project_model = ProjectModel.model_validate(response.json())
        return Project(self, project_model)

    def get_by_team(self, team_id: int) -> list[Project]:
        """Get all projects that belong to a team."""
        response = self._api_client.get(f"teams/{team_id}/projects", None, 5)
        projects: list[Project] = []
        for value in response.json():
            project_model = ProjectModel.model_validate(value)
            projects.append(Project(self, project_model))

        return projects

    def create(
        self, creation_schema: request_schemas.projects.CreationRequest, team_id: int
    ) -> Project:
        """Create a new project."""
        response = self._api_client.post(
            f"teams/{team_id}/projects", creation_schema, None, 5
        )
        return self.get_by_id(response.json()["id"])

    def delete(self, project_id: int) -> None:
        """Delete project by ID."""
        self._api_client.delete(f"projects/{project_id}", None, 5)

    def update(
        self, project_id: int, update_schema: request_schemas.projects.UpdateRequest
    ) -> Project:
        """Update project by ID."""
        response = self._api_client.put(
            f"projects/{project_id}", update_schema, None, 5
        )
        return self.get_by_id(response.json()["id"])
