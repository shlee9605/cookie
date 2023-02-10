import os
import uvicorn
from fastapi import FastAPI

from dotenv import load_dotenv

from models import connection
import routes

# dotenv config
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

# app runs
if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)

app = FastAPI()

# mongodb - odmantic - connect
app.add_event_handler("startup", connection.on_app_start)
app.add_event_handler("shutdown", connection.on_app_shutdown)

# routing
app.include_router(routes.router)