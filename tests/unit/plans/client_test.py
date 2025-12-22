"""Unit tests for Cherry Servers Python SDK plans client."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast

import cherryservers_sdk_python.plans
from tests.unit import helpers

if TYPE_CHECKING:
    from unittest import mock


def test_get_by_id_success(
    simple_plan: dict[str, Any],
    plans_client: cherryservers_sdk_python.plans.PlanClient,
) -> None:
    """Test successfully getting a plan by ID."""
    expected_api_resp = helpers.build_api_response(simple_plan, 200)
    cast("mock.Mock", plans_client._api_client.get).return_value = expected_api_resp
    plan = plans_client.get_by_id_or_slug(simple_plan["id"])

    assert plan.get_model() == cherryservers_sdk_python.plans.PlanModel.model_validate(
        simple_plan
    )

    cast("mock.Mock", plans_client._api_client.get).assert_called_with(
        f"plans/{simple_plan['id']}",
        {"fields": "plan,specs,pricing,region,href"},
        plans_client.request_timeout,
    )


def test_list_by_team(
    simple_plan: dict[str, Any],
    plans_client: cherryservers_sdk_python.plans.PlanClient,
) -> None:
    """Test successfully listing team plans."""
    expected_api_resp = helpers.build_api_response([simple_plan, simple_plan], 200)
    cast("mock.Mock", plans_client._api_client.get).return_value = expected_api_resp
    plans = plans_client.list_by_team(123456)

    for plan, expected_plan in zip(plans, [simple_plan, simple_plan], strict=False):
        assert (
            plan.get_model()
            == cherryservers_sdk_python.plans.PlanModel.model_validate(expected_plan)
        )

    cast("mock.Mock", plans_client._api_client.get).assert_called_with(
        "teams/123456/plans",
        {"fields": "plan,specs,pricing,region,href"},
        plans_client.request_timeout,
    )
