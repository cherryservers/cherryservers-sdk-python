"""Cherry Servers API client."""

from __future__ import annotations

from typing import Any

import requests

from cherryservers_sdk_python import _base, _version


class InvalidMethodError(Exception):
    """Invalid HTTP method used."""

    def __init__(self, method: str) -> None:
        super().__init__(f"Invalid method {method}")


class CherryApiClient:
    """Cherry Servers API client."""

    def __init__(
        self,
        token: str,
        api_endpoint_base: str = "https://api.cherryservers.com/v1/",
        user_agent_prefix: str = "",
    ) -> None:
        self._token = token
        self._api_endpoint_base = api_endpoint_base
        self._requests_session = requests.Session()
        self._headers = self._get_headers(user_agent_prefix)
        self._requests_session.headers.update(self._headers)

    def _get_headers(self, user_agent_suffix: str) -> dict[str, str]:
        return {
            "User-Agent": f"{user_agent_suffix}/cherryservers_sdk_python-python/"
            f"{_version.__version__} {requests.__name__}/{requests.__version__}",
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
                url, params=params, timeout=timeout, allow_redirects=False
            )
            # We need this to avoid dropping authentication headers, when redirect
            # uses HTTP, since that will be considered a different domain.
            if r.status_code in (301, 302):
                redirect_url = r.headers.get("Location")
                if redirect_url is not None:
                    r = self._send_request(
                        "GET", redirect_url, params=params, timeout=timeout
                    )
        if method == "POST":
            r = self._requests_session.post(
                url,
                params=params,
                timeout=timeout,
                data=data,
            )
        if method == "PUT":
            r = self._requests_session.put(
                url, params=params, timeout=timeout, data=data
            )
        if method == "PATCH":
            r = self._requests_session.patch(
                url, params=params, timeout=timeout, data=data
            )
        if method == "DELETE":
            r = self._requests_session.delete(url, params=params, timeout=timeout)
        if isinstance(r, requests.Response):
            try:
                r.raise_for_status()
            except requests.exceptions.HTTPError as e:
                raise requests.exceptions.HTTPError(e.response.text) from e
            return r
        raise InvalidMethodError(method)

    def get(
        self, path: str, params: dict[str, Any] | None = None, timeout: int = 10
    ) -> requests.Response:
        """GET to Cherry Servers API."""
        return self._send_request(
            "GET", self._api_endpoint_base + path, params, None, timeout
        )

    def post(
        self,
        path: str,
        data: _base.RequestSchema,
        params: dict[str, Any] | None = None,
        timeout: int = 10,
    ) -> requests.Response:
        """POST to Cherry Servers API."""
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
        data: _base.RequestSchema,
        params: dict[str, Any] | None = None,
        timeout: int = 10,
    ) -> requests.Response:
        """PUT to Cherry Servers API."""
        return self._send_request(
            "PUT",
            self._api_endpoint_base + path,
            params,
            data.model_dump_json(),
            timeout,
        )

    def patch(
        self,
        path: str,
        data: _base.RequestSchema,
        params: dict[str, Any] | None = None,
        timeout: int = 10,
    ) -> requests.Response:
        """PATCH to Cherry Servers API."""
        return self._send_request(
            "PATCH",
            self._api_endpoint_base + path,
            params,
            data.model_dump_json(),
            timeout,
        )

    def delete(
        self, path: str, params: dict[str, Any] | None = None, timeout: int = 10
    ) -> requests.Response:
        """DELETE to Cherry Servers API."""
        return self._send_request(
            "DELETE", self._api_endpoint_base + path, params, None, timeout
        )
