# CLAUDE.md

Guidance for Claude Code when working in this repository.

## Overview

`members-reader` is a zero-dependency Python package (src layout) that reads member CSV files into typed `Member` objects, plus a `members-reader` CLI. `hello.py` and the full `members.csv` are local-only and git-ignored; ignore them.

- `src/members_reader/`: `reader.py` (`read_members`, `iter_members`), `models.py`, `errors.py`, `cli.py`
- `examples/members_sample.csv`: 10-row sample used by tests and docs
- CSV columns: `id,first_name,last_name,email,gender,ip_address`

## Commands

```
pip install -e ".[dev]"
pytest
members-reader examples/members_sample.csv
```
