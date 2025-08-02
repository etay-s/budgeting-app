from dataclasses import dataclass

@dataclass
class BalanceRequest:
    income: int
    expenses: int

@dataclass
class BalanceResponse:
    balance: int