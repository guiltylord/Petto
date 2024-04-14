from fastapi import FastAPI
from fastapi_users import fastapi_users

from src.auth.base_config import auth_backend
app = FastAPI(
    title="Petto"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(),
    prefix="/auth",
    tags=["Auth"],
)

