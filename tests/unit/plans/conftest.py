"""Cherry Servers Python SDK plans unit test fixtures."""

from __future__ import annotations

import json
import pathlib
from unittest import mock

import pytest

import cherryservers_sdk_python.plans


@pytest.fixture
def plans_client() -> cherryservers_sdk_python.plans.PlanClient:
    """Initialize plan client fixture."""
    return cherryservers_sdk_python.plans.PlanClient(api_client=mock.MagicMock())


@pytest.fixture
def plan_resource(
    plan_path: pathlib.Path,
    plans_client: cherryservers_sdk_python.plans.PlanClient,
) -> cherryservers_sdk_python.plans.Plan:
    """Initialize plan resource fixture."""
    with pathlib.Path.open(plan_path, "r") as f:
        return cherryservers_sdk_python.plans.Plan(
            client=plans_client,
            model=cherryservers_sdk_python.plans.PlanModel.model_validate(json.load(f)),
        )


@pytest.fixture
def plan_path() -> pathlib.Path:
    """Path to plan response sample."""
    return (
        pathlib.Path(__file__).parent.parent.joinpath("testdata").joinpath("plan.json")
    )


@pytest.fixture
def plans_path() -> pathlib.Path:
    """Path to plans response sample."""
    return (
        pathlib.Path(__file__).parent.parent.joinpath("testdata").joinpath("plans.json")
    )
