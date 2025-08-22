from pydantic import BaseModel, NonNegativeFloat


class BalanceRequest(BaseModel):
    income: NonNegativeFloat
    expenses: NonNegativeFloat


class BalanceResponse(BaseModel):
    balance: NonNegativeFloat
