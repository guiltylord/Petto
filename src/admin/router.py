from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import HTMLResponse

from src.admin.htmlAdmin import htmlAdmin
from src.auth.models import user
from src.database import get_async_session

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/")
async def get_info():
    return HTMLResponse(htmlAdmin)


# @router.get("/")
# async def get_specific_operations(
#     user_id: int, session: AsyncSession = Depends(get_async_session)
# ):
#     query = select(user).where(user.c.id == user_id)
#     result = await session.execute(query)
#     return result.all()
