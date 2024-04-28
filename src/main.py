from fastapi import Depends
from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from src.admin.router_admin import router as router_admin, websocket_endpoint

# from src.admin.htmlAdmin import htmlAdmin
from src.auth.base_config import auth_backend
from src.auth.manager import get_user_manager
from src.auth.schemas import UserCreate, UserRead, UserCreateIn
from src.database import User

app = FastAPI(title="Petto")


@app.get("/user/{user_id}")
def get_user(user_id):
    return "not ready"


@app.post("/user/{user_id}")
def change_name(user_id: int, new_name):
    # fake_users[user_id] = new_name
    # return fake_users.get(user_id)
    return "not ready too"


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

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


current_user = fastapi_users.current_user()


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.email}"


@app.get("/unprotected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, noname"


app.include_router(router_admin)


app.websocket("/ws")(websocket_endpoint)
