from celery import Celery

celery_app = Celery(
    "ai_workflow_worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    include=["app.workers.tasks"],
)

celery_app.conf.task_track_started = True