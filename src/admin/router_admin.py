from fastapi import APIRouter, Depends
from fastapi_users import FastAPIUsers
from starlette.responses import HTMLResponse
from starlette.websockets import WebSocket, WebSocketDisconnect

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


async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()

            # Разделяем сообщение на команду и данные
            command, _, message_data = data.partition(":")

            if command == "get_hash_user":
                user_id = int(message_data)
                hash_user = await getHashUser(user_id)
                await websocket.send_text(f"Хэш юзера {message_data}: {hash_user}")
                print(hash_user)

            elif command == "sendAnother":
                result = await getRowCount()
                await websocket.send_text(
                    f"Кол-во зарегистрированных пользователей: {result}"
                )

            elif command == "getEcho":
                await websocket.send_text(f"Эхо: {message_data}")

            elif command == "get_user_data":
                user_id = int(message_data)  # Передаем user_id как целое число
                user_info = await getUserInfo(user_id, True)
                await websocket.send_text(str(user_info))
                print(user_info)
            elif command == "user_weight":
                user_id = int(message_data)  # Передаем user_id как целое число
                user_info = await getUserWeight(user_id)
                await websocket.send_text(str(user_info))
    except WebSocketDisconnect:
        print("Клиент отключился")
