"""Cherry Servers backup storage resource management module."""

from __future__ import annotations

from pydantic import Field

import cherry
from cherry import _models


class BackupStorageModel(_models.DefaultModel):
    """Cherry Server backup storage model.

    This model is frozen by default,
    since it represents an actual Cherry Servers backup storage resource state.

    Attributes:
        id (int): Backup storage ID.
        status (str): Backup storage status.
        state (str): Backup storage state.
        private_ip (str): Backup storage private IP.
        public_ip (str): Backup storage public IP.
        size_gigabytes (int): Backup storage total size in GB.
        used_gigabytes (int): Backup storage used size in GB.
        attached_to (cherry.servers.AttachedServerModel | None):
        The server to which to storage is attached to.

    """

    id: str = Field(description="Backup storage ID.")
    status: str = Field(description="Backup storage status.")
    state: str = Field(description="Backup storage state.")
    private_ip: str = Field(description="Backup storage private IP.")
    public_ip: str = Field(description="Backup storage public IP.")
    size_gigabytes: int = Field(description="Backup storage total size in GB.")
    used_gigabytes: int = Field(description="Backup storage used size in GB.")
    attached_to: cherry.servers.AttachedServerModel | None = Field(
        description="Server to which the storage is attached to.", default=None
    )
