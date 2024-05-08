from fastapi import Depends, HTTPException
from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from starlette.requests import Request
from starlette.responses import HTMLResponse

from src.admin.dao_user import getUserInfo
from src.admin.htmlAdmin import htmlAdmin
from src.admin.router_admin import router as router_admin, websocket_endpoint
from fastapi import FastAPI, Request, HTTPException
from starlette.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="src/auth")

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


# @app.get("/user/{user_id}")
# async def get_user(user_id: int):
#     return await getUserInfo(user_id)


@app.get("/user/{user_id}", response_class=HTMLResponse)
async def get_user(request: Request, user_id: int):
    user_info = await getUserInfo(user_id)
    if user_info is None:
        raise HTTPException(status_code=404, detail="User not found")
    return templates.TemplateResponse(
        "user_info.html", {"request": request, "user": user_info}
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


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.email}"


@app.get("/unprotected-route")
def protected_route():
    return f"Hello, noname"


app.include_router(router_admin)
app.websocket("/ws")(websocket_endpoint)


# @app.get("/")
# def main():
#     return HTMLResponse(htmlAdmin)
#
#
# @app.post("/")
# def main2():
#     return "loli"
