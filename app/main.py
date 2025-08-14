from quart import Quart, request
from quart_schema import QuartSchema
from app.config import settings
from app.routes import balance_bp, sign_up_bp, login_bp
from app.auth.jwt_utils import auth_required

app = Quart(__name__)
QuartSchema(app)

app.register_blueprint(balance_bp)
app.register_blueprint(sign_up_bp)
app.register_blueprint(login_bp)

@app.get('/')
@auth_required
async def hello():
    return 'hello world!'

def run() -> None:
    app.run(debug=settings.debug)