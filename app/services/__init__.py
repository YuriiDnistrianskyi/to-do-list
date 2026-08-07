from .orders.user_service import UserService
from .orders.task_service import TaskService
from .orders.email_service import EmailService

from app.repositories import user_repository, task_repository

user_service = UserService(user_repository)
task_service = TaskService(task_repository)

email_service = EmailService()
