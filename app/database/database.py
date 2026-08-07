from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from app.core.config import DATABASE_URL


from sqlalchemy.pool import NullPool


engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    poolclass=NullPool #
)

async_session = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

class Base(DeclarativeBase):
    pass

from .models.user import User
from .models.task import Task
