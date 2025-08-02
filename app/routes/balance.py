from quart import Blueprint, request
from quart_schema import validate_request, validate_response
from schemas.balance import BalanceRequest, BalanceResponse

balance_bp = Blueprint('balance', __name__)

@balance_bp.post('/balance')
@validate_request(BalanceRequest)
@validate_response(BalanceResponse)
async def balance(data: BalanceRequest) -> BalanceResponse:
    result = data.income - data.expenses
    return BalanceResponse(result)