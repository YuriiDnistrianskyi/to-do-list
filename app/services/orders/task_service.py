from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Boolean

from app.repositories.orders.user_repository import UserRepository
from app.services.base_service import BaseService
from app.repositories.orders.task_repository import TaskRepository
from app.database.models.task import Task
from app.schemes.task_schemes import CreateTaskScheme, UpdateTaskScheme
from app.exceptions.task_already_completed import TaskAlreadyCompleted
from app.database.database import async_session


class TaskService(BaseService[Task]):
    def __init__(self, repository: TaskRepository, user_repository: UserRepository):
        super().__init__(repository)
        self.repository: TaskRepository = repository
        self.user_repository: UserRepository = user_repository

    async def get_all_tasks(self, session: AsyncSession, status: str = None) -> list[Task]:
        if status is not None:
            if status == 'completed':
                tasks = await self.repository.get_all_tasks(session, is_complete=True)
            elif status == 'not_completed':
                tasks = await self.repository.get_all_tasks(session, is_complete=False)
            else:
                tasks = []
        else:
            tasks = await self.repository.get_all_tasks(session)
        return tasks

    async def create(self, schema: CreateTaskScheme, user_id: int, session: AsyncSession) -> Task:
        task = Task(
            description=schema.description,
            deadline=schema.deadline,
            is_completed=False,
            user_id=user_id,
        )

        user = await self.user_repository.get_by_id(user_id, session)

        from app.services import email_service

        await email_service.send(
            to=user.email,
            subject='Task Created',
            body='Created New Task'
        )

        await self.repository.add(task, session)
        return task


    async def update(self, obj_id: int, schema: UpdateTaskScheme, session: AsyncSession) -> Task:
        obj = await self.repository.get_by_id(obj_id, session)
        data = schema.model_dump(exclude_unset=True)

        if 'description' in data:
            obj.description = data['description']

        if 'deadline' in data:
            obj.deadline = data['deadline']

        await session.commit()
        return obj

    async def complete(self, obj_id: int, session: AsyncSession) -> Task:
        obj = await self.repository.get_by_id(obj_id, session)
        if obj.is_completed:
            raise TaskAlreadyCompleted("Task already completed")
        obj.is_completed = True

        await session.commit()
        return obj

    async def delete_expired_tasks(self):
        async with async_session() as session:
            await self.repository.delete_expired_tasks(session)
