import json
from pathlib import Path

import pytest

from members_reader import Member, MemberParseError, iter_members, read_members
from members_reader.cli import main

SAMPLE = Path(__file__).parent.parent / "examples" / "members_sample.csv"
HEADER = "id,first_name,last_name,email,gender,ip_address\n"


def test_read_sample():
    members = read_members(SAMPLE)
    assert len(members) == 10
    assert members[0] == Member(1, "Ber", "Turney", "bturney0@europa.eu", "Male", "246.210.126.30")
    assert members[0].full_name == "Ber Turney"


def test_iter_is_lazy():
    assert next(iter_members(SAMPLE)).id == 1


def test_missing_file():
    with pytest.raises(FileNotFoundError):
        read_members("nope.csv")


def test_missing_column(tmp_path):
    p = tmp_path / "bad.csv"
    p.write_text("id,first_name\n1,A\n")
    with pytest.raises(MemberParseError, match="missing column"):
        read_members(p)


def test_bad_id(tmp_path):
    p = tmp_path / "bad.csv"
    p.write_text(HEADER + "x,A,B,a@b.c,F,1.1.1.1\n")
    with pytest.raises(MemberParseError, match="line 2"):
        read_members(p)


def test_cli_names(capsys):
    assert main([str(SAMPLE), "--limit", "2"]) == 0
    assert capsys.readouterr().out.splitlines() == ["Ber Turney", "Catherine Dransfield"]


def test_cli_json(capsys):
    assert main([str(SAMPLE), "--format", "json", "--limit", "1"]) == 0
    assert json.loads(capsys.readouterr().out)[0]["email"] == "bturney0@europa.eu"


def test_cli_error(capsys):
    assert main(["nope.csv"]) == 1
    assert "error:" in capsys.readouterr().err
