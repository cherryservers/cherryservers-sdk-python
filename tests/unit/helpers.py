"""Unit test helpers."""

from __future__ import annotations

import json
from typing import Any

import requests


def build_api_response(
    resp_content: dict[str, Any] | list[dict[str, Any]], status_code: int
) -> requests.Response:
    """Initialize successful response for server GET request."""
    response = requests.Response()
    response.status_code = status_code
    response._content = json.dumps(resp_content).encode("utf-8")
    return response
