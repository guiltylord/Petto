from typing import Optional

from fastapi_users import schemas, models
from fastapi_users.schemas import BaseUserCreate
from pydantic import EmailStr, BaseModel


class UserRead(schemas.BaseUser[int]):
    id: int
    email: EmailStr
    username: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


class UserCreate(schemas.BaseUserCreate):
    id: int
    username: str
    email: EmailStr
    password: str
    role_id: int
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserCreateIn(BaseModel):
    username: str
    email: EmailStr
    password: str

    def create_update_dict(self) -> dict:
        # Верните словарь с полями, которые должны быть созданы или обновлены
        return self.dict()
