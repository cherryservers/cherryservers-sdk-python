"""Cherry Servers User related models."""

from __future__ import annotations

from typing import TypedDict


class UserModel(TypedDict):
    """Cherry Servers User object model."""

    id: int
    first_name: str
    last_name: str
    email: str
    email_verified: bool
    phone: str
    security_phone: str
    security_phone_verified: bool
    href: str
