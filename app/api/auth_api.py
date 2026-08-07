from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.dependencies import get_async_session
from app.schemes.auth_scheme import LoginScheme, RefreshScheme
from app.services import user_service
from app.exceptions.not_found import NotFound
from app.core.security import verify_password
from app.core.jwt import create_access_token, create_refresh_token, verify_token

auth_router = APIRouter()


@auth_router.post('/login')
async def login(
    data: LoginScheme,
    session: AsyncSession = Depends(get_async_session)
):
    try:
        user = await user_service.get_by_email(data.email, session)
        if not verify_password(user.password_hash, data.passwprd):
            raise HTTPException(status_code=400, detail="Incorrect password")

        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    except NotFound as ex:
        raise HTTPException(status_code=404, detail=str(ex))

@auth_router.post('/refresh')
async def refresh(
        data: RefreshScheme,
):
    try:
        payload = verify_token(data.refresh_token)
        access_token = create_access_token(payload['user_id'])
        refresh_token = create_refresh_token(payload['user_id'])
        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }
    except Exception as ex:
        raise HTTPException(status_code=400, detail=str(ex))

