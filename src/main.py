from fastapi import Depends
from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from src.admin.dao_user import getUserInfo
from src.admin.router_admin import router as router_admin, websocket_endpoint

# from src.admin.htmlAdmin import htmlAdmin
from src.auth.base_config import auth_backend
from src.auth.manager import get_user_manager
from src.auth.models import User
from src.auth.schemas import UserRead, UserCreateIn

app = FastAPI(title="Petto")

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
current_user = fastapi_users.current_user()


@app.get("/user/{user_id}")
async def get_user(user_id: int):
    return await getUserInfo(user_id)


@app.post("/user/{user_id}")
def change_name(user_id: int, new_name):
    return "not ready too"


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)


app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreateIn),
    prefix="/auth",
    tags=["auth"],
)


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.email}"


@app.get("/unprotected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, noname"


app.include_router(router_admin)


app.websocket("/ws")(websocket_endpoint)
