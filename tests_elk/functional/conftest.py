"""Описание фикстур."""

import asyncio

import pytest

pytestmark = pytest.mark.asyncio


@pytest.fixture(scope='session')
def event_loop():
    """Функция.

    Yields:
        int: The next number in the range of 0 to `n` - 1.
    """
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()
