from app.celery_app import celery
import asyncio

from app.services import task_service


@celery.task
def remind_about_tasks():
    asyncio.run(task_service.remind_about_tasks())
