from __future__ import annotations

import abc
from typing import TYPE_CHECKING, Generic, TypeVar

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from cherryservers_sdk_python import _client


class ResourceModel(BaseModel, abc.ABC):
    model_config = ConfigDict(frozen=True)


class ResourceClient(abc.ABC):  # noqa: B024
    """Cherry Servers resource client base."""

    def __init__(
        self, api_client: _client.CherryApiClient, request_timeout: int = 120
    ) -> None:
        """Initialize a Cherry Servers resource client."""
        self._api_client = api_client
        self._request_timeout = request_timeout

    @property
    def request_timeout(self) -> int:
        """API request timeout in seconds."""
        return self._request_timeout

    @request_timeout.setter
    def request_timeout(self, value: int) -> None:
        """Set API request timeout in seconds."""
        self._request_timeout = value


C = TypeVar("C", bound=ResourceClient)
T = TypeVar("T", bound=ResourceModel)


class Resource(Generic[C, T], abc.ABC):
    def __init__(self, client: C, model: T) -> None:
        """Initialize a Cherry Servers resource."""
        self._model = model
        self._client = client

    def get_model(self) -> T:
        """Get resource model.

        This model is frozen, since it represents actual resource state.
        """
        return self._model


class RequestSchema(BaseModel, abc.ABC):
    """Cherry Servers base API request schema."""
