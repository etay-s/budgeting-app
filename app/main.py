from quart import Quart
from quart_schema import QuartSchema
from app.config import settings
from app.routes import balance_bp, auth_bp
from app.auth import auth_required

app = Quart(__name__)
QuartSchema(
    app,
    security_schemes={
        "bearer_auth": {"type": "http", "scheme": "bearer", "bearer_format": "JWT"}
    },
)

app.register_blueprint(balance_bp)
app.register_blueprint(auth_bp)


@app.get("/")
@auth_required
async def hello():
    return "hello world!"


def run() -> None:
    app.run(debug=settings.debug)
