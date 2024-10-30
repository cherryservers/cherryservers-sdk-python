"""Cherry Servers pricing model."""

from __future__ import annotations

from pydantic import Field

from cherry import _models


class PricingModel(_models.DefaultModel):
    """Cherry Servers pricing model.

    This model is frozen by default,
    since it represents an actual Cherry Servers pricing resource state.

    Attributes:
        price (float): Price.
        taxed (bool): Whether tax is applied.
        currency (str): Currency type.
        unit (str): Time unit type.

    """

    price: float = Field(description="Price.")
    taxed: bool = Field(description="Whether tax is applied.")
    currency: str = Field(description=" Currency type.")
    unit: str = Field(description="Time unit type.")
