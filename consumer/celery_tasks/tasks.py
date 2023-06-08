import celery


class PrimeNumbersSearchTask(celery.Task):
    name = 'prime_numbers_search_task'

    def run(self, payload: dict[str:list[int]]) -> list[int]:
        """placeholder method"""
        pass
