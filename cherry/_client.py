from __future__ import annotations

from typing import Any

import requests

from ._version import __version__


class InvalidMethodError(Exception):
    def __init__(self, method: str) -> None:
        super().__init__(f"Invalid method {method}")


class CherryApiClient:
    def __init__(
        self,
        token: str,
        api_endpoint: str = "https://api.cherryservers.com/v1/",
        user_agent_context: str = "",
    ) -> None:
        self._token = token
        self._api_endpoint = api_endpoint
        self._requests_session = requests.Session()
        self._headers = self._get_headers(user_agent_context)

    def _get_headers(self, user_agent_context: str) -> dict[str, str]:
        return {
            "User-Agent": f"{user_agent_context}/cherry-python/{__version__} {requests.__name__}/{requests.__version__}",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self._token}",
        }

    def _send_request(
        self,
        method: str,
        url: str,
        params: dict[str, Any] | None = None,
        payload: dict[str, Any] | None = None,
        timeout: int = 10,
    ) -> requests.Response:
        if method == "GET":
            return self._requests_session.get(
                url, params=params, timeout=timeout, headers=self._headers
            )
        if method == "POST":
            return self._requests_session.post(
                url, params=params, timeout=timeout, headers=self._headers, data=payload
            )
        if method == "PUT":
            return self._requests_session.put(
                url, params=params, timeout=timeout, headers=self._headers, data=payload
            )
        if method == "DELETE":
            return self._requests_session.delete(
                url, params=params, timeout=timeout, headers=self._headers
            )
        raise InvalidMethodError(method)

    def get(
        self, url: str, params: dict[str, Any] | None = None, timeout: int = 10
    ) -> requests.Response:
        return self._send_request("GET", url, params, None, timeout)

    def post(
        self,
        url: str,
        payload: dict[str, Any],
        params: dict[str, Any] | None = None,
        timeout: int = 10,
    ) -> requests.Response:
        return self._send_request("POST", url, params, payload, timeout)

    def put(
        self,
        url: str,
        payload: dict[str, Any],
        params: dict[str, Any] | None = None,
        timeout: int = 10,
    ) -> requests.Response:
        return self._send_request("PUT", url, params, payload, timeout)

    def delete(
        self, url: str, params: dict[str, Any] | None = None, timeout: int = 10
    ) -> requests.Response:
        return self._send_request("DELETE", url, params, None, timeout)
