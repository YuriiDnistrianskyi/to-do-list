from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.services import task_service
from app.schemes.task_schemes import CreateTaskScheme, UpdateTaskScheme
from app.database.dependencies import get_async_session
from app.exceptions.not_found import NotFound
from app.exceptions.task_already_completed import TaskAlreadyCompleted


task_router = APIRouter()

@task_router.get('/tasks')
async def get_tasks(
        session: AsyncSession = Depends(get_async_session)
):
    try:
        tasks = await task_service.get_all(session)
        return {
            'tasks': tasks
        }
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

@task_router.get('/tasks/{task_id')
async def get_task(
        task_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    try:
        task = await task_service.get_one(task_id, session)
        return {
            'task': task
        }
    except NotFound as ex:
        raise HTTPException(status_code=404, detail=str(ex))
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

@task_router.post('/tasks')
async def create_task(
        data: CreateTaskScheme,
        session: AsyncSession = Depends(get_async_session)
):
    try:
        task = await task_service.create(data, session)
        return {
            'task': task
        }
    except NotFound as ex:
        raise HTTPException(status_code=404, detail=str(ex))
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))


@task_router.patch('/tasks/{task_id')
async def update_task(
        task_id: int,
        data: UpdateTaskScheme,
        session: AsyncSession = Depends(get_async_session)
):
    try:
        task = await task_service.update(task_id, data, session)
        return {
            'task': task
        }
    except NotFound as ex:
        raise HTTPException(status_code=404, detail=str(ex))
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

@task_router.post('/tasks/{task_id}/complete')
async def complete_task(
        task_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    try:
        task = await task_service.complete(task_id, session)
        return {
            'task': task
        }
    except NotFound as ex:
        raise HTTPException(status_code=404, detail=str(ex))
    except TaskAlreadyCompleted as ex:
        raise HTTPException(status_code=400, detail=str(ex))
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

@task_router.delete('/tasks/{task_id}')
async def delete_task(
        task_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    try:
        await task_service.delete(task_id, session)
        return {
            'message': 'task deleted'
        }
    except NotFound as ex:
        raise HTTPException(status_code=404, detail=str(ex))
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

