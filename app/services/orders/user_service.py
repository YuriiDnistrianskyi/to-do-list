from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from app.services.base_service import BaseService
from app.repositories.orders.user_repository import UserRepository
from app.database.models.user import User
from app.schemes.user_schemes import CreateUserScheme, UpdateUserScheme
from app.core.security import create_hash
from app.exceptions.user_already_exists import UserAlreadyExists


class UserService(BaseService[User]):
    def __init__(self, repository: UserRepository):
        super().__init__(repository)
        self.repository: UserRepository = repository

    async def get_by_email(self, email: str, session: AsyncSession) -> User:
        user = await self.repository.get_by_email(email, session)
        return user

    async def create(self, schema: CreateUserScheme, session: AsyncSession) -> User:
        user = User(
            name=schema.name,
            email=schema.email,
            password_hash=create_hash(schema.password)
        )

        try:
            await self.repository.add(user, session)
        except IntegrityError:
            raise UserAlreadyExists('User already exists')

        from app.services import email_service
        await email_service.send(
            to=schema.email,
            subject='User created',
            body='User created. So Welcome!',
        )
        return user


    async def update(self, obj_id: int, schema: UpdateUserScheme, session: AsyncSession) -> User:
        obj = await self.repository.get_by_id(obj_id, session)
        data = schema.model_dump(exclude_unset=True)

        if 'name' in data:
            obj.name = data['name']

        await session.commit()
        return obj
