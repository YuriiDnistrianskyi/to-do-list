from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey

from app.database.database import Base


class Task(Base):
    __tablename__ = 'task'

    id: Mapped[Integer] = mapped_column(Integer, primary_key=True, autoincrement=True)
    description: Mapped[String] = mapped_column(String) #
    deadline: Mapped[DateTime] = mapped_column(DateTime(timezone=True))
    is_completed: Mapped[Boolean] = mapped_column(Boolean, default=False, nullable=False)
    user_id: Mapped[Integer] = mapped_column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='tasks')
