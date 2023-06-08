import random

from celery_tasks.tasks import PrimeNumbersSearchTask
from celery_tasks.utils import create_worker_from


class PrimeNumbersSearchTaskImpl(PrimeNumbersSearchTask):

    @staticmethod
    def miller_rabin(n, k=10):
        """Miller-Rabin algorithm for the probabilistic determination of a prime number."""
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False

        r, d = 0, n - 1
        while d % 2 == 0:
            r += 1
            d //= 2

        def witness(a):
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                return True
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    return True
            return False

        for _ in range(k):
            a = random.randint(2, n - 2)
            if not witness(a):
                return False
        return True

    def run(self, payload: dict[str:list[int]]):
        """Work that Celery task executes."""
        numbers = payload['numbers']
        if len(numbers) == 0:
            return numbers

        return list(filter(self.miller_rabin, numbers))


app, _ = create_worker_from(PrimeNumbersSearchTaskImpl)

if __name__ == '__main__':
    app.worker_main()
