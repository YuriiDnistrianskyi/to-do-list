import asyncio

from app.celery_app import celery
from app.services import task_service


@celery.task
def delete_expired_tasks():
    asyncio.run(task_service.delete_expired_tasks())
