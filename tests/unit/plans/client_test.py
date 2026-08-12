"""Unit tests for Cherry Servers Python SDK plans client."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

import cherryservers_sdk_python.plans
from tests.unit import helpers

if TYPE_CHECKING:
    import pathlib
    from unittest import mock


def test_get_by_id_success(
    plan_path: pathlib.Path,
    plans_client: cherryservers_sdk_python.plans.PlanClient,
) -> None:
    """Test successfully getting a plan by ID."""
    expected_api_resp = helpers.fake_response(plan_path, 200)
    cast("mock.Mock", plans_client._api_client.get).return_value = expected_api_resp
    want_plan_model = cherryservers_sdk_python.plans.PlanModel.model_validate(
        expected_api_resp.json()
    )
    plan = plans_client.get_by_id_or_slug(want_plan_model.id)

    assert want_plan_model == plan.get_model()

    cast("mock.Mock", plans_client._api_client.get).assert_called_with(
        f"plans/{want_plan_model.id}",
        {"fields": "plan,specs,pricing,region,softwares,href"},
        plans_client.request_timeout,
    )


def test_list_by_team(
    plans_path: pathlib.Path,
    plans_client: cherryservers_sdk_python.plans.PlanClient,
) -> None:
    """Test successfully listing team plans."""
    expected_api_resp = helpers.fake_response(plans_path, 200)
    cast("mock.Mock", plans_client._api_client.get).return_value = expected_api_resp
    plans = plans_client.list_by_team(123456)
    want_plan_models = [
        cherryservers_sdk_python.plans.PlanModel.model_validate(p)
        for p in expected_api_resp.json()
    ]

    assert len(plans) == len(want_plan_models)
    for plan, want_plan_model in zip(plans, want_plan_models, strict=True):
        assert want_plan_model == plan.get_model()

    cast("mock.Mock", plans_client._api_client.get).assert_called_with(
        "teams/123456/plans",
        {"fields": "plan,specs,pricing,region,softwares,href"},
        plans_client.request_timeout,
    )
