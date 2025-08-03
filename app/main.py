from quart import Quart, request
from quart_schema import QuartSchema
from config import settings
from routes import balance_bp, sign_up_bp

app = Quart(__name__)
QuartSchema(app)

app.register_blueprint(balance_bp)
app.register_blueprint(sign_up_bp)

@app.get('/')
async def hello():
    return 'hello world!'

if __name__ == "__main__":
    app.run(debug=settings.debug)