from celery import Celery
from celery.schedules import crontab

celery = Celery(
    "todo",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    include=["app.tasks.clear_tasks"]
)

celery.conf.beat_schedule = {
    "delete-expired-tasks": {
        "task": "app.tasks.clear_tasks.delete_expired_tasks",
        "schedule": 300.00
    }
}
