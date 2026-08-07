from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String

from app.database.database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[Integer] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[String] = mapped_column(String)
    email: Mapped[String] = mapped_column(String, unique=True)
    password_hash: Mapped[String] = mapped_column(String)

    tasks = relationship(
        'Task',
        back_populates='user',
        cascade='all, delete-orphan',
        passive_deletes=True
    )
