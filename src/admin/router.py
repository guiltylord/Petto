from fastapi import APIRouter
from starlette.responses import HTMLResponse
from starlette.websockets import WebSocket, WebSocketDisconnect

from src.admin.htmlAdmin import htmlAdmin

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/")
async def get_info():
    return HTMLResponse(htmlAdmin)


def get_user_count():
    return "1 fu"


def another_function():
    return "2 fu"


async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()

            # Разделяем сообщение на команду и данные
            command, _, message_data = data.partition(":")

            if command == "get_user_count":
                user_count = get_user_count()
                await websocket.send_text(f"Количество пользователей: {user_count}")
            elif command == "sendAnother":
                result = another_function()
                await websocket.send_text(f"Результат другой команды: {result}")
            elif command == "getEcho":
                await websocket.send_text(f"Эхо: {message_data}")
    except WebSocketDisconnect:
        print("Клиент отключился")
