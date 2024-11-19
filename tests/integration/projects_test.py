"""Test cherry projects module functionality."""

from __future__ import annotations

import pytest
import requests

import cherry


class TestProject:
    """Test Project functionality."""

    @pytest.fixture(scope="class")
    def project(
        self, facade: cherry.facade.CherryApiFacade, team_id: int
    ) -> cherry.projects.Project:
        """Initialize a Cherry Servers Project."""
        creation_req = cherry.projects.CreationRequest(
            name="cherry-python-sdk-project-test"
        )
        project = facade.projects.create(creation_req, team_id=team_id)

        project_model = project.get_model_copy()

        assert project_model.name == creation_req.name

        return project

    def test_get_by_id(
        self, project: cherry.projects.Project, facade: cherry.facade.CherryApiFacade
    ) -> None:
        """Test getting a single project by ID."""
        project_model = project.get_model_copy()
        retrieved_project = facade.projects.get_by_id(project_model.id)
        retrieved_project_model = retrieved_project.get_model_copy()

        assert retrieved_project_model.name == project_model.name

    def test_get_by_team(
        self,
        project: cherry.projects.Project,
        facade: cherry.facade.CherryApiFacade,
        team_id: int,
    ) -> None:
        """Test getting all projects that belong to a team."""
        retrieved_projects = facade.projects.get_by_team(team_id)
        retrieved_project_models = [
            model.get_model_copy() for model in retrieved_projects
        ]
        project_model = project.get_model_copy()

        assert any(
            project_model.name == retrieved_project_model.name
            for retrieved_project_model in retrieved_project_models
        )

    def test_update(self, project: cherry.projects.Project) -> None:
        """Test updating a project."""
        update_req = cherry.projects.UpdateRequest(
            name="cherry-python-sdk-project-test-updated", bgp=True
        )
        project.update(update_req)

        updated_model = project.get_model_copy()

        assert updated_model.name == update_req.name

    def test_delete(
        self, project: cherry.projects.Project, facade: cherry.facade.CherryApiFacade
    ) -> None:
        """Test deleting a project."""
        project.delete()
        project_model = project.get_model_copy()

        with pytest.raises(requests.exceptions.HTTPError):
            facade.projects.get_by_id(project_model.id)
