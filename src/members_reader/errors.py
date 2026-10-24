"""Exceptions raised by members-reader."""


class MemberParseError(ValueError):
    """The CSV file is not a valid members file.

    Raised when required columns are missing or a row cannot be parsed.
    """
