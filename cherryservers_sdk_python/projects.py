"""Cherry Servers project resource management module."""

from __future__ import annotations

from pydantic import Field

from cherryservers_sdk_python import _base


class ProjectBGPModel(_base.ResourceModel):
    """Cherry Servers project BGP model.

    This model is frozen by default,
    since it represents an actual Cherry Servers project BGP resource state.

    Attributes:
        enabled (bool | None): Whether BGP is enabled for the project.
        local_asn (int | None): Local ASN of the project.

    """

    enabled: bool | None = Field(
        description="Whether BGP is enabled for the project.", default=None
    )
    local_asn: int | None = Field(description="Local ASN of the project.", default=None)


class ProjectModel(_base.ResourceModel):
    """Cherry Servers project model.

    This model is frozen by default,
    since it represents an actual Cherry Servers project resource state.

    Attributes:
        id (int): Project ID.
        name (str | None): Project name.
        bgp (cherryservers_sdk_python.projects.ProjectBGPModel | None): Project BGP.
        href (str | None): Project href.

    """

    id: int = Field(description="Project ID.")
    name: str | None = Field(description="Project name.", default=None)
    bgp: ProjectBGPModel | None = Field(description="Project BGP.", default=None)
    href: str | None = Field(description="Project href.", default=None)


class CreationRequest(_base.RequestSchema):
    """Cherry Servers project creation request schema.

    Attributes:
        name (str): Project name.
        bgp (bool): Whether BGP is enabled for the project. Defaults to False.

    """

    name: str = Field(description="Project name.")
    bgp: bool = Field(
        description="Whether BGP is enabled for the project. Defaults to False.",
        default=False,
    )


class UpdateRequest(_base.RequestSchema):
    """Cherry Servers project update request schema.

    Attributes:
        name (str | None): Project name.
        bgp (bool | None): Whether BGP is enabled for the project..

    """

    name: str | None = Field(description="Project name.", default=None)
    bgp: bool | None = Field(
        description="Whether BGP is enabled for the project.", default=None
    )


class ProjectClient(_base.ResourceClient):
    """Cherry Servers project client.

    Manage Cherry Servers project resources.
    This class should typically be initialized by
    :class:`cherryservers_sdk_python.facade.CherryApiFacade`.

    Example:
        .. code-block:: python

            facade = cherryservers_sdk_python.facade.CherryApiFacade(token="my-token")

            # Retrieve a project.
            existing_project = facade.projects.get_by_id(123456)

            # Create project.
            req = cherryservers_sdk_python.projects.CreationRequest(
                name = "my-project"
            )
            project = facade.projects.create(req, 123456)

            # Update project.
            upd_req = cherryservers_sdk_python.projects.UpdateRequest(
                name = "my-project-updated",
                bgp = True
            )
            project.update(upd_req)

            # Remove project.
            project.delete()

    """

    def get_by_id(self, project_id: int) -> Project:
        """Retrieve a project by ID."""
        response = self._api_client.get(
            f"projects/{project_id}",
            None,
            5,
        )
        project_model = ProjectModel.model_validate(response.json())
        return Project(self, project_model)

    def list_by_team(self, team_id: int) -> list[Project]:
        """Get all projects that belong to a team."""
        response = self._api_client.get(f"teams/{team_id}/projects", None, 5)
        projects: list[Project] = []
        for value in response.json():
            project_model = ProjectModel.model_validate(value)
            projects.append(Project(self, project_model))

        return projects

    def create(self, creation_schema: CreationRequest, team_id: int) -> Project:
        """Create a new project."""
        response = self._api_client.post(
            f"teams/{team_id}/projects", creation_schema, None, 5
        )
        return self.get_by_id(response.json()["id"])

    def delete(self, project_id: int) -> None:
        """Delete project by ID."""
        self._api_client.delete(f"projects/{project_id}", None, 5)

    def update(self, project_id: int, update_schema: UpdateRequest) -> Project:
        """Update project by ID."""
        response = self._api_client.put(
            f"projects/{project_id}", update_schema, None, 5
        )
        return self.get_by_id(response.json()["id"])


class Project(_base.Resource[ProjectClient, ProjectModel]):
    """Cherry Servers project resource.

    This class represents an existing Cherry Servers resource
    and should only be initialized by :class:`ProjectClient`.
    """

    def delete(self) -> None:
        """Delete Cherry Servers project resource."""
        self._client.delete(self._model.id)

    def update(self, update_schema: UpdateRequest) -> None:
        """Update Cherry Servers project resource."""
        updated = self._client.update(self._model.id, update_schema)
        self._model = updated.get_model()

    def get_id(self) -> int:
        """Get resource ID."""
        return self._model.id
