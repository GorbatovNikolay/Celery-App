from typing import Type

from celery import Celery, Task


def create_worker_from(WorkerClass: Type[Task], celery_config='celery_tasks.celery_config') -> tuple[Celery, Task]:
    """Function that creates Celery app and registers tasks."""
    assert issubclass(WorkerClass, Task)
    app = Celery()
    app.config_from_object(celery_config)
    app.conf.update(task_default_queue=WorkerClass.name)
    worker_task = app.register_task(WorkerClass())

    return app, worker_task
