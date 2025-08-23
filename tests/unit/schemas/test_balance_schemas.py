import pytest
from pydantic import ValidationError
from app.schemas.balance import BalanceRequest


class TestBalanceRequestSchema:
    @pytest.mark.parametrize("income", [1000, 0, "0", "1000", 1000.50, "1000.50"])
    @pytest.mark.parametrize("expenses", [500, 0, "0", "500", 500.25, "500.25"])
    def test_request_accepts_valid_input(self, income, expenses):
        request = BalanceRequest(income=income, expenses=expenses)
        assert request.income == float(income)
        assert request.expenses == float(expenses)

    def test_request_rejects_negative_income(self):
        with pytest.raises(ValidationError):
            BalanceRequest(income=-100, expenses=500)

    def test_request_rejects_negative_expenses(self):
        with pytest.raises(ValidationError):
            BalanceRequest(income=100, expenses=-50)

    def test_request_rejects_invalid_input(self):
        with pytest.raises(ValidationError):
            BalanceRequest(income="invalid", expenses=500)
