"""Cherry Servers Python SDK projects unit test fixtures."""

from __future__ import annotations

from typing import Any
from unittest import mock

import pytest

import cherryservers_sdk_python.projects


@pytest.fixture
def projects_client() -> cherryservers_sdk_python.projects.ProjectClient:
    """Initialize project client fixture."""
    return cherryservers_sdk_python.projects.ProjectClient(api_client=mock.MagicMock())


@pytest.fixture
def project_resource(
    simple_project: dict[str, Any],
    projects_client: cherryservers_sdk_python.projects.ProjectClient,
) -> cherryservers_sdk_python.projects.Project:
    """Initialize project resource fixture."""
    return cherryservers_sdk_python.projects.Project(
        client=projects_client,
        model=cherryservers_sdk_python.projects.ProjectModel.model_validate(
            simple_project
        ),
    )


@pytest.fixture
def simple_project() -> dict[str, Any]:
    """Initialize simple project fixture."""
    return {
        "id": 123456,
        "name": "test",
        "bgp": {"enabled": True, "local_asn": 12345},
        "href": "/projects/123456",
        "traffic": [
            {
                "id": "73121...3ac6ea",
                "used_bytes": 88027,
                "allowance_bytes": 0,
                "limited_bytes": 0,
                "name": "Europe & N. America (USA)",
                "regions": [
                    {
                        "href": "/regions/1",
                        "bgp": {
                            "hosts": ["123.123.123.123", "123.123.123.123"],
                            "asn": 12345,
                        },
                    },
                    {
                        "href": "/regions/2",
                        "bgp": {
                            "hosts": ["123.123.123.123", "123.123.123.123"],
                            "asn": 12345,
                        },
                    },
                    {
                        "href": "/regions/3",
                        "bgp": {
                            "hosts": ["123.123.123.123", "123.123.123.123"],
                            "asn": 12345,
                        },
                    },
                    {
                        "href": "/regions/5",
                        "bgp": {
                            "hosts": ["123.123.123.123", "123.123.123.123"],
                            "asn": 12345,
                        },
                    },
                ],
            }
        ],
    }
