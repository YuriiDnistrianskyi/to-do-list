from fastapi import FastAPI

from .auth_api import auth_router
from .task_api import task_router
from .user_api import user_router


def include_routers(app: FastAPI):
    app.include_router(auth_router, prefix="/api/auth", tags=["auth"])
    app.include_router(task_router, prefix="/api/tasks", tags=["task"])
    app.include_router(user_router, prefix="/api/users", tags=["user"])