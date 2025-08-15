from quart import Quart, request
from quart_schema import QuartSchema
from app.config import settings
from app.routes import balance_bp, sign_up_bp, login_bp
from app.auth import auth_required

app = Quart(__name__)
QuartSchema(
    app,
    security_schemes={
        "bearer_auth": {
            "type": "http",
            "scheme": "bearer",
            "bearer_format": "JWT"
        }
    },
)

app.register_blueprint(balance_bp)
app.register_blueprint(sign_up_bp)
app.register_blueprint(login_bp)

@app.get('/')
@auth_required
async def hello():
    return 'hello world!'

def run() -> None:
    app.run(debug=settings.debug)