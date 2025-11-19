from quart import Blueprint
from quart_schema import validate_request, validate_response
from app.schemas.user import SignUpRequest, SignUpResponse, LoginRequest, LoginResponse
from app.services.auth_service import register_user, login_user
from app.routes.utils.http_status_codes import HTTPStatusCodes
from app.types import Response

auth_bp = Blueprint("auth", __name__)


@auth_bp.post("/sign-up")
@validate_request(SignUpRequest)
@validate_response(SignUpResponse, status_code=HTTPStatusCodes.CREATED)
async def sign_up(req: SignUpRequest) -> Response[SignUpResponse]:
    user_id = await register_user(
        name=req.name, email=req.email, password=req.password.get_secret_value()
    )
    return SignUpResponse(id=user_id), HTTPStatusCodes.CREATED


@auth_bp.post("/login")
@validate_request(LoginRequest)
@validate_response(LoginResponse, status_code=HTTPStatusCodes.OK)
async def login(req: LoginRequest) -> Response[LoginResponse]:
    token = await login_user(email=req.email, password=req.password.get_secret_value())
    return LoginResponse(access_token=token), HTTPStatusCodes.OK
