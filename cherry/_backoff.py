from __future__ import annotations

import abc
import time
import typing
from random import uniform
from typing import Protocol


class DeploymentTimeoutError(Exception):
    """Deployment timeout occurred."""

    def __init__(self, msg: str) -> None:
        super().__init__(f"{msg}")


class ResourceTimeoutError(Exception):
    """Resource timeout occurred."""

    def __init__(self, msg: str) -> None:
        super().__init__(f"{msg}")


class ResourceModelWithStatus(Protocol):
    """Resource model than contains a status field."""

    status: str | None


class DeployableResource(abc.ABC):
    """A resource that is deployable."""

    @abc.abstractmethod
    def get_model_copy(self) -> ResourceModelWithStatus: ...

    @abc.abstractmethod
    def refresh(self) -> None: ...


class RefreshableResource(abc.ABC):
    """A resource that is deployable."""

    @abc.abstractmethod
    def refresh(self) -> None: ...


def wait_for_deployment(
    resource: DeployableResource,
    timeout: float,
) -> None:
    """Wait for a resource to be deployed.

    :param DeployableResource resource: Resource to wait for.
    :param float timeout: Timeout in seconds.

    :raises DeploymentTimeoutError: If timeout occurs.
    """
    model_copy = resource.get_model_copy()
    retries = 0
    while model_copy.status != "deployed":
        delay = _get_exponential_delay(retries)
        if delay > timeout:
            msg = f"timeout waiting for {resource.__class__.__name__} to deploy"
            raise DeploymentTimeoutError(msg)
        time.sleep(delay)
        resource.refresh()
        model_copy = resource.get_model_copy()
        retries += 1


def wait_for_resource_condition(
    resource: RefreshableResource,
    timeout: float,
    condition: typing.Callable[[], bool],
) -> None:
    """Refresh resource until condition is met.

    :param RefreshableResource resource: Resource to wait for.
    :param float timeout: Timeout in seconds.
    :param typing.Callable[[], bool] condition: Condition to wait for.

    :raises ResourceTimeoutError: If timeout occurs.
    """
    retries = 0
    while not condition():
        delay = _get_exponential_delay(retries)
        if delay > timeout:
            msg = f"timeout waiting for {resource.__class__.__name__} to deploy"
            raise ResourceTimeoutError(msg)
        time.sleep(delay)
        resource.refresh()
        retries += 1


def _get_exponential_delay(retries: int) -> float:
    """Get exponential delay in seconds.

    :param int retries: The number of retries that have occurred so far.
    """
    max_delay: float = 20
    delay: float = (2 * 2**retries / 2) + uniform(0, (2 * 2**retries / 2))  # noqa: S311
    return min(delay, max_delay)
