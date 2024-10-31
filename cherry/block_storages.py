"""Cherry Servers EBS resource management module."""

from __future__ import annotations

from pydantic import Field

from cherry import _models
from cherry.ips import AttachedServerModel
from cherry.regions import RegionModel


class BlockStorageModel(_models.DefaultModel):
    """Cherry Servers Elastic Block Storage model.

    This model is frozen by default,
    since it represents an actual Cherry Servers EBS resource state.

    Attributes:
        id (int): EBS ID.
        name (str): EBS name.
        href (str): EBS href.
        size (int): EBS size.
        allow_edit_size (bool): Whether size can be edited.
        unit (str): Size measurement unit.
        attached_to (cherry.ips.AttachedServerModel):
        EBS attached server data.
        vlan_id (str): EBS VLAN ID.
        vlan_ip (str): EBS VLAN IP address.
        initiator (str): EBS initiator.
        discovery_ip (str): EBS discovery IP address.
        region (cherry.regions.RegionModel): Region data.

    """

    id: int = Field(description="EBS ID.")
    name: str = Field(description="EBS name.")
    href: str = Field(description="EBS href.")
    size: int = Field(description="EBS size.")
    allow_edit_size: bool = Field(description="Whether size can be edited.")
    unit: str = Field(description="Size measurement unit.")
    attached_to: AttachedServerModel = Field(description="EBS attached server model.")
    vlan_id: str = Field(description="EBS VLAN ID.")
    vlan_ip: str = Field(description="EBS VLAN IP address.")
    initiator: str = Field(description="EBS initiator.")
    discovery_ip: str = Field(description="EBS discovery IP address.")
    region: RegionModel = Field(description="Region data.")
