def test_truth():
    assert 2 + 2 == 4

# Async smoke test (verifies pytest-asyncio works)
import asyncio
import pytest

@pytest.mark.asyncio
async def test_async_sleep():
    await asyncio.sleep(0)
    assert False
