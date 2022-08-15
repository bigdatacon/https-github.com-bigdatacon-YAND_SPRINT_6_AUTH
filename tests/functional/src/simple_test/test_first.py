"""Tests."""

import json

import pytest

pytestmark = pytest.mark.asyncio


def test_assert(datadir, shared_datadir):
    """Простой тест.

    Args:
        datadir: The first parameter.
        shared_datadir: The second parameter. Defaults to None.
    """
    test_data = json.loads((shared_datadir / 'test_data.json').read_text())
    expected = json.loads((datadir / 'response.json').read_text())
    assert test_data == expected
