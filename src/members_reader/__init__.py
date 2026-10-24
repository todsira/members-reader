"""members-reader: read member records from CSV files.

Quickstart::

    from members_reader import read_members

    for member in read_members("members.csv"):
        print(member.full_name, member.email)
"""

from .errors import MemberParseError
from .models import Member
from .reader import iter_members, read_members

__version__ = "0.1.0"

__all__ = ["Member", "MemberParseError", "iter_members", "read_members", "__version__"]
