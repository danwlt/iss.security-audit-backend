import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.routes.login_route import router as login_router
from app.routes.result_route import router as result_router
from app.routes.command_route import router as command_router


logging.basicConfig(filename="app.log", level=logging.DEBUG)

logger = logging.getLogger(__name__)

load_dotenv()

app = FastAPI()

origins = [
    "http://localhost:8080",
    "http://localhost:80",
    "http://vue_frontend:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login_router, tags=['Login'], prefix='/token')
app.include_router(result_router, tags=['Result'], prefix='/result')
app.include_router(command_router, tags=['Command'], prefix='/command')
