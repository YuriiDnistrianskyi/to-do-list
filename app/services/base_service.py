from sqlalchemy.ext.asyncio import AsyncSession
from typing import Generic, TypeVar

from app.repositories.base_repository import BaseRepository


T = TypeVar("T")

class BaseService(Generic[T]):

    def __init__(self, repository: BaseRepository[T]):
        self.repository = repository


    async def get_all(self, session: AsyncSession) -> list[T]:
        return await self.repository.get_all(session)


    async def get_by_id(self, obj_id: int, session: AsyncSession) -> T:
        return await self.repository.get_by_id(obj_id, session)


    async def delete(self, obj_id: int, session: AsyncSession) -> None:
        await self.repository.delete(obj_id, session)
