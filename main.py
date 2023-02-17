import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv

from models import connection
import routes

# dotenv config
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

# app runs
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

app = FastAPI()

# CORS config
# origins = [
#     "*",
#     "http://192.168.0.7",
#     "http://localhost", 
#     "http://localhost:8080", 
# ]
origins=["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# mongodb - odmantic - connect
app.add_event_handler("startup", connection.on_app_start)
app.add_event_handler("shutdown", connection.on_app_shutdown)

# routing
app.include_router(routes.router)

