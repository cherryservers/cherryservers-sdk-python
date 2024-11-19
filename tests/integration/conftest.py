"""Integration test configuration."""

from __future__ import annotations

import os

import pytest

import cherry


@pytest.fixture(scope="package")
def facade() -> cherry.facade.CherryApiFacade:
    """Initialize Cherry API facade."""
    token = os.environ.get("CHERRY_AUTH_KEY")
    assert token, "CHERRY_AUTH_KEY environment variable is not set"
    return cherry.facade.CherryApiFacade(token=token, user_agent_suffix="test")


@pytest.fixture(scope="package")
def team_id() -> int:
    """Get a pre-initialized Cherry Servers team."""
    team_id = os.environ.get("CHERRY_TEST_TEAM_ID")
    assert team_id, "CHERRY_TEST_TEAM_ID environment variable is not set"
    return int(team_id)
