FROM python:3.11
ADD ./consumer/prime_numbers_search/requirements.txt /
ADD ./consumer/prime_numbers_search/main.py /
ADD ./consumer/prime_numbers_search/tests.py /
ADD ./consumer/celery_tasks/ /celery_tasks/
RUN pip3 install -r requirements.txt
ENTRYPOINT celery -A main worker --concurrency=4 --loglevel=info -n prime_numbers_search_worker.%h