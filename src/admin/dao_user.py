# dao.py – DAO (Data Access Object) является распространённым шаблоном и подходит для файлов,
# содержащих классы или функции, которые производят непосредственный доступ к данным.

from sqlalchemy import select, func, exc

from src.auth.models import User
from src.database import async_session_maker


# TODO: сделать проверку исключений везде чтоб сервак не падал
async def getRowCount():
    async with async_session_maker() as session:
        try:
            result = await session.execute(select(func.count()).select_from(User))
        except ValueError:
            return "User with current id not found"
        count = result.scalar_one()
        return count


async def getHashUser(user_id: int):
    async with async_session_maker() as session:
        query = select(User).where(User.id == user_id)
        result = await session.execute(query)
        user = result.scalar_one_or_none()
        if user:
            user_data = f"User with id {user_id} has hash {user.hashed_password}"
            return user_data
        return f"User with id {user_id} does not exist."


async def getUserInfo(user_id: int, is_admin=False):
    async with async_session_maker() as session:
        query = select(User).where(User.id == user_id)
        result = await session.execute(query)
        user = result.scalar_one_or_none()

        if user:
            # Преобразование экземпляра модели User в словарь
            if is_admin:
                user_data = {
                    column.name: getattr(user, column.name)
                    for column in user.__table__.columns
                }
            else:
                user_data = {
                    "id": user.id,
                    "username": user.username,
                    "name": user.name,
                    "surname": user.surname,
                    "email": user.email,
                }
            return user_data
        else:
            return f"User with id {user_id} does not exist."


async def getUserWeight(user_id: int):
    async with async_session_maker() as session:
        # Сначала извлекаем пользователя по ID
        stmt = select(User).where(User.id == user_id)
        result = await session.execute(stmt)
        user_instance = result.scalar_one_or_none()

        if user_instance:
            size_sum = sum(
                func.pg_column_size(getattr(user_instance, column.name))
                for column in User.__table__.columns
            )
            result = await session.execute(select(size_sum))
            row_size = result.scalar_one()
            return f"User with id {user_id} has {row_size} bytes of data."

        else:
            return f"User with id {user_id} does not exist."
