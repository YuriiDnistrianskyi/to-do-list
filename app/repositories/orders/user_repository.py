from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.repositories.base_repository import BaseRepository
from app.database.models.user import User
from app.exceptions.not_found import NotFound


class UserRepository(BaseRepository[User]):
    _model = User

    async def get_by_email(self, email: str, session: AsyncSession) -> User:
        stmt = select(self._model).where(User.email == email)
        result = await session.execute(stmt)
        user = result.scalar_one_or_none()

        if user is None:
            raise NotFound(f'User with email {email} not found')
        return user

