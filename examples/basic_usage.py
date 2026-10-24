"""Run from the repo root: python examples/basic_usage.py"""

from members_reader import read_members

members = read_members("examples/members_sample.csv")
print(f"Loaded {len(members)} members")
for m in members[:3]:
    print(f"{m.id}: {m.full_name} <{m.email}>")
