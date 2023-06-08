from typing import Generator, Final

from celery import group

from celery_tasks.tasks import PrimeNumbersSearchTask
from celery_tasks.utils import create_worker_from

NUMBER_OF_PARTS: Final = 16


def _split(arr: list[int], number_of_parts: int) -> Generator:
    """Function that splits the array 'a' into n equal parts."""
    quotient, remainder = divmod(len(arr), number_of_parts)
    result = (
        arr[i * quotient + min(i, remainder):(i + 1) * quotient + min(i + 1, remainder)]
        for i in range(number_of_parts)
    )
    return result


async def find_prime_numbers(numbers: list[int]) -> list[int]:
    """Function that gets prime numbers from list using Celery workers."""
    _, find_worker = create_worker_from(PrimeNumbersSearchTask)

    task_group = group(
        find_worker.s({'numbers': segment}) for segment in _split(numbers, NUMBER_OF_PARTS)
    )
    celery_result = task_group.apply_async()
    result_values = celery_result.get()

    return [j for i in result_values for j in i]
