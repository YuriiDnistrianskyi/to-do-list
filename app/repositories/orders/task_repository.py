from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from datetime import datetime, UTC, timedelta

from app.repositories.base_repository import BaseRepository
from app.database.models.task import Task


class TaskRepository(BaseRepository[Task]):
    _model = Task

    async def get_all_tasks(self, session: AsyncSession, is_complete: bool=None) -> list[Task]:
        if is_complete is None:
            stmt = select(self._model)
        else:
            stmt = select(self._model).where(self._model.is_completed == is_complete)
        result = await session.execute(stmt)
        tasks = result.scalars().all()
        return list(tasks)

    async def delete_expired_tasks(self, session: AsyncSession):
        stmt = delete(self._model).where(self._model.deadline < datetime.now(UTC))

        await session.execute(stmt)
        await session.commit()

    async def get_due_soon(self, session: AsyncSession) -> list[Task]:
        stmt = select(self._model).where(
            self._model.deadline > datetime.now(UTC),
            self._model.deadline < datetime.now(UTC) + timedelta(days=1)
        )

        result = await session.execute(stmt)
        tasks = result.scalars().all()
        return list(tasks)
