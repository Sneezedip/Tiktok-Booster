import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import parse_cooldown

@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("5 minutes 30 seconds", 330),
        ("2 minutes", 120),
        ("45 seconds", 45),
        ("", 0),
    ]
)
def test_parse_cooldown(input_text, expected):
    assert parse_cooldown(input_text) == expected
