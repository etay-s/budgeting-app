from app.main import app
from .exceptions import AppError
from quart_schema import RequestSchemaValidationError
from app.routes.utils.http_status_codes import HTTPStatusCodes


@app.errorhandler(AppError)
async def handle_app_error(e: AppError):
    return {"title": e.title, "error": e.message}, e.http_status_code


@app.errorhandler(RequestSchemaValidationError)
async def handle_request_validation_error(e: RequestSchemaValidationError):
    return {
        "title": "Validation Error",
        "error": str(e.validation_error),
    }, HTTPStatusCodes.UNPROCESSABLE_CONTENT
