from datetime import datetime, UTC
import asyncio

from app.celery_app import celery
from app.services import task_service


@celery.task
def delete_expired_tasks():
    print("Task")
    asyncio.run(task_service.delete_expired_tasks())
