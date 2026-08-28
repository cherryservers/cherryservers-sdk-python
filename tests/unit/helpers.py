"""Unit test helpers."""

from __future__ import annotations

import json
import pathlib
from typing import TYPE_CHECKING, Any

import requests

if TYPE_CHECKING:
    import pathlib


def build_api_response(
    resp_content: dict[str, Any] | list[dict[str, Any]], status_code: int
) -> requests.Response:
    """Initialize successful response for server GET request."""
    response = requests.Response()
    response.status_code = status_code
    response._content = json.dumps(resp_content).encode("utf-8")
    return response


def fake_response(content: pathlib.Path, status: int) -> requests.Response:
    """Build a fake API response with the given content and status."""
    response = requests.Response()
    response.status_code = status
    response._content = content.read_bytes()
    response.encoding = "utf-8"
    response.headers["Content-Type"] = "application/json"
    return response
