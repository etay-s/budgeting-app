from quart import Quart
from config import settings

app = Quart(__name__)

@app.route('/')
async def hello():
    return 'hello world!'

if __name__ == "__main__":
    app.run(debug=settings.debug)