from __future__ import annotations

import abc
import time
import typing
from random import uniform


class ResourceTimeoutError(Exception):
    """Resource timeout occurred."""

    def __init__(self, msg: str) -> None:
        super().__init__(f"{msg}")


class RefreshableResource(abc.ABC):
    """A resource that is deployable."""

    @abc.abstractmethod
    def refresh(self) -> None: ...


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
