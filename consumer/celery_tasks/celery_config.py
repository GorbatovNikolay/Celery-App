from typing import Final

from celery_tasks.rabbitmq_config import (
    RABBITMQ_USER,
    RABBITMQ_PWD,
    RABBITMQ_HOST,
    RABBITMQ_PORT
)

broker_url: Final = f'pyamqp://{RABBITMQ_USER}:{RABBITMQ_PWD}@{RABBITMQ_HOST}:{RABBITMQ_PORT}'
result_backend: Final = 'rpc://'
