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
