from quart import Blueprint, request
from quart_schema import validate_request, validate_response, validate_headers
from app.schemas.balance import BalanceRequest, BalanceResponse
from app.auth import auth_required, AuthHeaders

balance_bp = Blueprint('balance', __name__)

@balance_bp.post('/balance')
@validate_request(BalanceRequest)
@validate_response(BalanceResponse)
@validate_headers(AuthHeaders)
@auth_required
async def balance(data: BalanceRequest) -> BalanceResponse:
    result = data.income - data.expenses
    return BalanceResponse(result)