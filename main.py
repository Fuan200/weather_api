from fastapi import FastAPI
from uvicorn import run

from server.weather import weather

app = FastAPI()

@app.get('/')
async def home():
    return 'Hello World'

app.include_router(weather)

if __name__ == '__main__':
    run(app, host='127.0.0.1', port=8000)