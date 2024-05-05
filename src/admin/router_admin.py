from fastapi import APIRouter, Depends
from fastapi_users import FastAPIUsers
from starlette.responses import HTMLResponse
from starlette.websockets import WebSocketDisconnect

from src.admin.dao_user import (
    getUserInfo,
    getRowCount,
    getHashUser,
    getUserWeight,
)
from src.admin.htmlAdmin import htmlAdmin
from src.auth.base_config import auth_backend
from src.auth.manager import get_user_manager
from src.auth.models import User

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
current_user = fastapi_users.current_user()

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/")
async def get_info(user: User = Depends(current_user)):
    if user.is_superuser:
        return HTMLResponse(htmlAdmin)
    return "U have no access"


from fastapi import WebSocket


async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            await process_received_data(await websocket.receive_text(), websocket)
    except WebSocketDisconnect:
        print("Клиент отключился")


# Разделяем сообщение на команду и данные
async def process_received_data(data, websocket):
    command, _, message_data = data.partition(":")
    if command == "sendAnother":
        await process_send_another_command(websocket)
    elif command == "get_hash_user" and message_data:
        await process_get_hash_user_command(message_data, websocket)
    elif command == "getEcho":
        await process_get_echo_command(message_data, websocket)
    elif command == "get_user_data" and message_data:
        await process_get_user_data_command(message_data, websocket)
    elif command == "user_weight" and message_data:
        await process_user_weight_command(message_data, websocket)
    else:
        await websocket.send_text(
            "Введите Id пользователя или используйте валидную команду."
        )


async def process_send_another_command(websocket):
    result = await getRowCount()
    await websocket.send_text(f"Кол-во зарегистрированных пользователей: {result}")


async def process_get_hash_user_command(user_id_str, websocket):
    user_id = int(user_id_str)
    hash_user = await getHashUser(user_id)
    await websocket.send_text(hash_user)


async def process_get_echo_command(message_data, websocket):
    await websocket.send_text(f"Эхо: {message_data}")


async def process_get_user_data_command(user_id_str, websocket):
    user_id = int(user_id_str)
    user_info = await getUserInfo(user_id, True)
    await websocket.send_text(str(user_info))


async def process_user_weight_command(user_id_str, websocket):
    user_id = int(user_id_str)
    user_info = await getUserWeight(user_id)
    await websocket.send_text(str(user_info))
