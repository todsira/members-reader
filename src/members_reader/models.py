"""Data model for a single member."""

from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class Member:
    """One row of a members CSV file.

    Attributes:
        id: Unique integer identifier.
        first_name: Given name.
        last_name: Family name.
        email: Email address.
        gender: Gender as written in the file (free text).
        ip_address: IP address as a string (not validated).
    """

    id: int
    first_name: str
    last_name: str
    email: str
    gender: str
    ip_address: str

    @property
    def full_name(self) -> str:
        """``first_name`` and ``last_name`` joined by a space."""
        return f"{self.first_name} {self.last_name}"

    def to_dict(self) -> dict[str, object]:
        """Return the member as a plain dict (handy for JSON)."""
        return asdict(self)
