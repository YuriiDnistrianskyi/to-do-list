from sqlalchemy.ext.asyncio import AsyncSession

from app.services.base_service import BaseService
from app.database.models.task import Task
from app.schemas.task_schemas import CreateTaskSchema, UpdateTaskSchema


class TaskService(BaseService[Task]):
    async def create(self, schema: CreateTaskSchema, user_id: int, session: AsyncSession) -> Task:
        task = Task(
            description=schema.description,
            deadline=schema.deadline,
            is_completed=False,
            user_id=user_id,
        )

        await self.repository.add(task, session)
        return task


    async def update(self, obj_id: int, schema: UpdateTaskSchema, session: AsyncSession) -> Task:
        obj = await self.repository.get_by_id(obj_id, session)
        data = schema.model_dump(exclude_unset=True)

        if 'description' in data:
            obj.description = data['description']

        if 'deadline' in data:
            obj.deadline = data['deadline']

        return obj
