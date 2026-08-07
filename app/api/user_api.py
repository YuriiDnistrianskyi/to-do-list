from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.services import user_service
from app.schemes.user_schemes import CreateUserScheme, UpdateUserScheme
from app.database.dependencies import get_async_session
from app.exceptions.not_found import NotFound
from app.exceptions.user_already_exists import UserAlreadyExists


user_router = APIRouter()

@user_router.get('/users/{user_id')
async def get_user(
        user_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    try:
        user = await user_service.get_one(user_id, session)
        return {
            'user': user
        }
    except NotFound as ex:
        raise HTTPException(status_code=404, detail=str(ex))
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

@user_router.post('/users')
async def create_user(
        data: CreateUserScheme,
        session: AsyncSession = Depends(get_async_session)
):
    try:
        user = await user_service.create_user(data, session)
        return {
            'user': user
        }
    except NotFound as ex:
        raise HTTPException(status_code=404, detail=str(ex))
    except UserAlreadyExists as ex:
        raise HTTPException(status_code=400, detail=str(ex))
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

@user_router.patch('/users/{user_id')
async def update_user(
        user_id: int,
        data: UpdateUserScheme,
        session: AsyncSession = Depends(get_async_session)
):
    try:
        user = await user_service.update(user_id, data, session)
        return {
            'user': user
        }
    except NotFound as ex:
        raise HTTPException(status_code=404, detail=str(ex))
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

@user_router.delete('/users/{user_id}')
async def delete_user(
        user_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    try:
        await user_service.delete(user_id, session)
        return {
            'message': 'user deleted'
        }
    except NotFound as ex:
        raise HTTPException(status_code=404, detail=str(ex))
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

