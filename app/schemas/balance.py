from pydantic import BaseModel


class BalanceRequest(BaseModel):
    income: int
    expenses: int


class BalanceResponse(BaseModel):
    balance: int
