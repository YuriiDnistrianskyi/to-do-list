from celery import Celery
from celery.schedules import crontab
from datetime import timedelta


celery = Celery(
    "todo",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    include=["app.tasks.clear_tasks", "app.tasks.task_reminder"]
)

celery.conf.beat_schedule = {
    "delete-expired-tasks": {
        "task": "app.tasks.clear_tasks.delete_expired_tasks",
        "schedule": timedelta(hours=1)
    },
    "remind-expired-tasks": {
        "task": "app.tasks.task_reminder.remind_about_tasks",
        "schedule": timedelta(days=1)
    }
}
