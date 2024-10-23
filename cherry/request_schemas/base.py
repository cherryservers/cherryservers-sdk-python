"""Cherry Servers base API request schema."""

from __future__ import annotations

import abc

from pydantic import BaseModel


class CherryRequestSchema(BaseModel, abc.ABC):
    """Cherry Servers base API request schema."""
