from quart import Blueprint
from quart_schema import validate_request, validate_response
from app.schemas.balance import BalanceRequest, BalanceResponse
from app.auth import auth_required
from app.services.balance_service import check_balance
from app.routes.utils.http_status_codes import HTTPStatusCodes

balance_bp = Blueprint("balance", __name__)


@balance_bp.post("/balance")
@validate_request(BalanceRequest)
@validate_response(BalanceResponse)
@auth_required
async def get_balance(req: BalanceRequest) -> BalanceResponse:
    result = await check_balance(income=req.income, expenses=req.expenses)
    return BalanceResponse(balance=result), HTTPStatusCodes.OK
