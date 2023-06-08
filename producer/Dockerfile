FROM python:3.11
ADD ./producer/requirements.txt /
ADD ./producer/main.py /
ADD ./producer/tasks.py /
ADD ./producer/tests.py /
ADD ./producer/celery_tasks/ /celery_tasks/
RUN pip install --no-cache-dir --upgrade -r /requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
