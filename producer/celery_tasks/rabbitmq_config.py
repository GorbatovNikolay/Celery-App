import os

from typing import Final

RABBITMQ_PORT: Final = int(os.getenv('RABBITMQ_PORT', '5672'))
RABBITMQ_PWD: Final = os.getenv('RABBITMQ_DEFAULT_PASS', 'mypass')
RABBITMQ_USER: Final = os.getenv('RABBITMQ_DEFAULT_USER', 'admin')
RABBITMQ_HOST: Final = os.getenv('RABBITMQ_DEFAULT_USER', 'rabbit')
