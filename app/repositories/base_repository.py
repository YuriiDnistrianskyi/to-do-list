from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Generic, TypeVar


T = TypeVar("T")

class BaseRepository(Generic[T]):
    _model = T

    async def get_all(self, session: AsyncSession) -> list[T]:
        stmt = select(self._model)
        list_ = await session.execute(stmt)
        result = list_.scalars().all()
        return result

    async def get_by_id(self, id: int, session: AsyncSession) -> T:
        obj = await session.get(self._model, id)
        if not obj:
            raise HTTPException(status_code=404)
        return obj

    async def add(self, obj: T, session: AsyncSession) -> None:
        session.add(obj)

    # async def update(self, id: int, new_obj: T, session: AsyncSession) -> None:
    #     pass

    async def delete(self, id: int, session: AsyncSession) -> None:
        obj = await session.get(self._model, id)
        if not obj:
            raise HTTPException(status_code=404)
        await session.delete(obj)