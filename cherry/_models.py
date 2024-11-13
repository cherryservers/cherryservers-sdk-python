from __future__ import annotations

import abc

from pydantic import BaseModel, ConfigDict


class DefaultModel(BaseModel, abc.ABC):
    model_config = ConfigDict(frozen=True)


class CherryRequestSchema(BaseModel, abc.ABC):
    """Cherry Servers base API request schema."""
