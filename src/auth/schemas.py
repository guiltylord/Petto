from fastapi_users import schemas, models
from pydantic import EmailStr, BaseModel


class UserRead(schemas.BaseUser[int]):
    id: int
    email: EmailStr
    username: str
    name: str
    surname: str


class UserCreateIn(BaseModel):
    username: str
    name: str
    surname: str
    email: EmailStr
    password: str

    def create_update_dict(self) -> dict:
        return self.dict()
