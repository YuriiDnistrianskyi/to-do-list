from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from app.services.base_service import BaseService
from app.database.models.user import User
from app.schemas.user_schemas import CreateUserSchema, UpdateUserSchema
from app.core.security import create_hash
from app.exceptions.user_already_exists import UserAlreadyExists


class UserService(BaseService[User]):
    async def create(self, schema: CreateUserSchema, session: AsyncSession) -> User:
        user = User(
            name=schema.name,
            email=schema.email,
            password_hash=create_hash(schema.password)
        )

        try:
            await self.repository.add(user, session)
        except IntegrityError:
            raise UserAlreadyExists('User already exists')
        return user


    async def update(self, obj_id: int, schema: UpdateUserSchema, session: AsyncSession) -> User:
        obj = await self.repository.get_by_id(obj_id, session)
        data = schema.model_dump(exclude_unset=True)

        if 'name' in data:
            obj.name = data['name']

        return obj
