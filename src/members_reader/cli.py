"""Command-line interface: ``members-reader FILE``."""

from __future__ import annotations

import argparse
import itertools
import json
import sys
from collections.abc import Sequence

from . import __version__
from .errors import MemberParseError
from .reader import iter_members


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="members-reader", description="Print members from a CSV file.")
    parser.add_argument("file", help="path to the members CSV file")
    parser.add_argument("--format", choices=["names", "json", "emails"], default="names",
                        help="output format (default: names)")
    parser.add_argument("--limit", type=int, metavar="N", help="only print the first N members")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    args = parser.parse_args(argv)

    try:
        members = iter_members(args.file)
        if args.limit is not None:
            members = itertools.islice(members, args.limit)
        if args.format == "json":
            json.dump([m.to_dict() for m in members], sys.stdout, indent=2)
            print()
        else:
            for m in members:
                print(m.full_name if args.format == "names" else m.email)
    except (OSError, MemberParseError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
