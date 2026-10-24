# members-reader

[![CI](https://github.com/OWNER/members-reader/actions/workflows/ci.yml/badge.svg)](https://github.com/OWNER/members-reader/actions)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Read member records from a CSV file into typed Python objects. Pure standard library, no dependencies, Python 3.9+.

## Install

```
pip install git+https://github.com/OWNER/members-reader
```

## Quickstart

```python
from members_reader import read_members

for m in read_members("members.csv"):
    print(m.full_name, m.email)
```

## CSV format

A header row is required with these columns (any order, extra columns ignored):

`id, first_name, last_name, email, gender, ip_address`

See [examples/members_sample.csv](examples/members_sample.csv).

## API

| Name | Description |
|---|---|
| `read_members(path, encoding="utf-8") -> list[Member]` | Read the whole file. |
| `iter_members(path, encoding="utf-8") -> Iterator[Member]` | Lazy, for large files. |
| `Member` | Frozen dataclass: `id: int`, `first_name`, `last_name`, `email`, `gender`, `ip_address` (all `str`). Also `.full_name` and `.to_dict()`. |
| `MemberParseError` | Subclass of `ValueError`. Raised for missing columns or a non-integer `id` (message includes the line number). |

A missing file raises the standard `FileNotFoundError`.

```python
from members_reader import iter_members, MemberParseError

try:
    emails = [m.email for m in iter_members("members.csv")]
except MemberParseError as e:
    print("Bad file:", e)
```

## Command line

```
members-reader members.csv                  # one full name per line
members-reader members.csv --format emails
members-reader members.csv --format json --limit 5
```

Exit code is `0` on success, `1` on error (message on stderr).

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md). Licensed under the [MIT License](LICENSE).
