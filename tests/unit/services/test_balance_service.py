import pytest
from app.services.balance_service import check_balance

class TestBalanceService:
    @pytest.mark.asyncio
    @pytest.mark.parametrize("income, expenses, expected_result", [
        (1000, 500, 500),
        (500, 1000, -500),
        (1000, 1000, 0),
        (0, 0, 0),
        (100, 0, 100),
        (0, 100, -100)
    ])
    async def test_returns_correct_balance(self, income, expenses, expected_result):
        response = await check_balance(income, expenses)
        assert response == expected_result