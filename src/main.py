from fastapi import Depends
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi_users import FastAPIUsers
from starlette.templating import Jinja2Templates
from src.admin.dao_user import getUserInfo
from src.admin.router_admin import router as router_admin, websocket_endpoint
from src.chat.models import message
from src.tasks.models import Order
from src.tasks.hz import (
    create_order,
    get_email_template_dashboard,
)

templates = Jinja2Templates(directory="src/templates")

from src.auth.base_config import auth_backend
from src.auth.manager import get_user_manager
from src.auth.models import User
from src.auth.schemas import UserRead, UserCreateIn

app = FastAPI(title="MotylDDX")

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
current_user = fastapi_users.current_user()


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


@app.post("/order")
def add_order(order: Order):
    return f"{create_order.delay(order.customer_name, order.order_quantity)}"


@app.post("/dashboard")
def get_dashboard_report(user=Depends(current_user)):
    return f"{get_email_template_dashboard.delay(user.username)}"


@app.get("/me")
async def protected_route(request: Request, user: User = Depends(current_user)):
    user_info = await getUserInfo(user.id)
    return templates.TemplateResponse(
        "user_info.html", {"request": request, "user": user_info}
    )


manager = ChatManager()


@app.post("/lilka")
def lolka(receiver_id: str, content: str, user=Depends(current_user)):
    return manager.send_message(user.id, receiver_id, content)


@app.get("/not-auth")
def protected_route(request: Request):
    return templates.TemplateResponse("not_auth.html", {"request": request})


app.include_router(router_admin)
app.websocket("/ws")(websocket_endpoint)
