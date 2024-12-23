"""Unit test helpers."""

from __future__ import annotations

import json
from typing import Any, TypeAlias

import requests


def build_api_response(
    resp_content: dict[str, Any] | list[dict[str, Any]] | JSON, status_code: int
) -> requests.Response:
    """Initialize successful response for server GET request."""
    response = requests.Response()
    response.status_code = status_code
    response._content = json.dumps(resp_content).encode("utf-8")
    return response


def get_integer_id(resource: JSON) -> int:
    """Get resource ID."""
    assert isinstance(resource, dict)
    assert resource.get("id", None) is not None
    assert isinstance(resource["id"], int)
    return resource["id"]


JSON: TypeAlias = dict[str, "JSON"] | list["JSON"] | str | int | float | bool | None
