"""Functions for reading members CSV files."""

from __future__ import annotations

import csv
from collections.abc import Iterator
from os import PathLike
from pathlib import Path

from .errors import MemberParseError
from .models import Member

REQUIRED_COLUMNS = ("id", "first_name", "last_name", "email", "gender", "ip_address")


def iter_members(path: str | PathLike[str], encoding: str = "utf-8") -> Iterator[Member]:
    """Lazily yield :class:`Member` objects from a CSV file.

    Use this for large files, since rows are not held in memory.

    Args:
        path: Path to a CSV file with a header row containing
            ``id, first_name, last_name, email, gender, ip_address``.
        encoding: File encoding. Defaults to ``"utf-8"``.

    Yields:
        One :class:`Member` per data row.

    Raises:
        FileNotFoundError: If ``path`` does not exist.
        MemberParseError: If columns are missing or a row has a non-integer id.
    """
    with Path(path).open(newline="", encoding=encoding) as f:
        reader = csv.DictReader(f)
        missing = [c for c in REQUIRED_COLUMNS if c not in (reader.fieldnames or [])]
        if missing:
            raise MemberParseError(f"{path}: missing column(s): {', '.join(missing)}")
        for row in reader:
            try:
                member_id = int(row["id"])
            except (TypeError, ValueError):
                raise MemberParseError(
                    f"{path}: line {reader.line_num}: invalid id {row['id']!r}"
                ) from None
            yield Member(
                id=member_id,
                first_name=row["first_name"],
                last_name=row["last_name"],
                email=row["email"],
                gender=row["gender"],
                ip_address=row["ip_address"],
            )


def read_members(path: str | PathLike[str], encoding: str = "utf-8") -> list[Member]:
    """Read every member in a CSV file into a list.

    See :func:`iter_members` for arguments and exceptions.

    Example:
        >>> members = read_members("examples/members_sample.csv")
        >>> members[0].full_name
        'Ber Turney'
    """
    return list(iter_members(path, encoding))
