from __future__ import annotations

from typing import TYPE_CHECKING, Any

import requests

from cherry import _version

if TYPE_CHECKING:
    from cherry.request_schemas import base as base_request


class InvalidMethodError(Exception):
    def __init__(self, method: str) -> None:
        super().__init__(f"Invalid method {method}")


class CherryApiClient:
    def __init__(
        self,
        token: str,
        api_endpoint_base: str = "https://api.cherryservers.com/v1/",
        user_agent_suffix: str = "",
    ) -> None:
        self._token = token
        self._api_endpoint_base = api_endpoint_base
        self._requests_session = requests.Session()
        self._headers = self._get_headers(user_agent_suffix)

    def _get_headers(self, user_agent_suffix: str) -> dict[str, str]:
        return {
            "User-Agent": f"{user_agent_suffix}/cherry-python/{_version.__version__} {requests.__name__}/{requests.__version__}",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self._token}",
        }

    def _send_request(
        self,
        method: str,
        url: str,
        params: dict[str, Any] | None = None,
        data: str | None = None,
        timeout: int = 10,
    ) -> requests.Response:
        r = None
        if method == "GET":
            r = self._requests_session.get(
                url, params=params, timeout=timeout, headers=self._headers
            )
        if method == "POST":
            r = self._requests_session.post(
                url, params=params, timeout=timeout, headers=self._headers, data=data
            )
        if method == "PUT":
            r = self._requests_session.put(
                url,
                params=params,
                timeout=timeout,
                headers=self._headers,
                data=data,
            )
        if method == "DELETE":
            r = self._requests_session.delete(
                url, params=params, timeout=timeout, headers=self._headers
            )
        if isinstance(r, requests.Response):
            r.raise_for_status()
            return r
        raise InvalidMethodError(method)

    def get(
        self, path: str, params: dict[str, Any] | None = None, timeout: int = 10
    ) -> requests.Response:
        return self._send_request(
            "GET", self._api_endpoint_base + path, params, None, timeout
        )

    def post(
        self,
        path: str,
        data: base_request.CherryRequestSchema,
        params: dict[str, Any] | None = None,
        timeout: int = 10,
    ) -> requests.Response:
        return self._send_request(
            "POST",
            self._api_endpoint_base + path,
            params,
            data.model_dump_json(),
            timeout,
        )

    def put(
        self,
        path: str,
        data: base_request.CherryRequestSchema,
        params: dict[str, Any] | None = None,
        timeout: int = 10,
    ) -> requests.Response:
        return self._send_request(
            "PUT",
            self._api_endpoint_base + path,
            params,
            data.model_dump_json(),
            timeout,
        )

    def delete(
        self, path: str, params: dict[str, Any] | None = None, timeout: int = 10
    ) -> requests.Response:
        return self._send_request(
            "DELETE", self._api_endpoint_base + path, params, None, timeout
        )
