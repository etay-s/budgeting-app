from app.routes.utils.http_status_codes import HTTPStatusCodes


class AppError(Exception):
    http_status_code = HTTPStatusCodes.BAD_REQUEST
    title = "Bad Request"

    def __init__(self, message: str = "Request could not be processed"):
        super().__init__(message)
        self.message = message


class UnauthorizedError(AppError):
    http_status_code = HTTPStatusCodes.UNAUTHORIZED
    title = "Unauthorized"


class PermissionDeniedError(AppError):
    http_status_code = HTTPStatusCodes.FORBIDDEN
    title = "Permission Denied"


class NotFound(AppError):
    http_status_code = HTTPStatusCodes.NOT_FOUND
    title = "Not Found"


class AlreadyExist(AppError):
    http_status_code = HTTPStatusCodes.CONFLICT
    title = "Already Exist"
