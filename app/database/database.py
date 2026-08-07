from sqlalchemy.ext.asyncio import create_async_engine, AsyncSessin
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from app.core.config import DATABASE_URL


engine = create_async_engine(
    DATABASE_URL,
    echo=True
)

async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

class Base(DeclarativeBase):
    pass
