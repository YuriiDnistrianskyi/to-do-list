from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Boolean

from app.repositories.base_repository import BaseRepository
from app.database.models.task import Task


class TaskRepository(BaseRepository[Task]):
    _model = Task

    async def get_all_tasks(self, session: AsyncSession, is_complete: bool=None) -> list[Task]:
        if is_complete is None:
            stmt = select(self._model)
        else:
            stmt = select(self._model).where(self._model.is_completed == is_complete)
        list_ = await session.execute(stmt)
        result = list_.scalars().all()
        return result
