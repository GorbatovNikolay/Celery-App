from fastapi import FastAPI

from tasks import find_prime_numbers

app = FastAPI()


@app.get("/ping")
async def ping():
    """An endpoint to ping."""
    return {"message": "OK"}


@app.post("/prime-numbers/{start}/{end}")
async def get_prime_numbers(first: int, last: int):
    """An endpoint to get prime numbers from interval between start and end values."""
    if first > last:
        return {'message': 'Error, first is bigger than last!'}
    prime_numbers: list[int] = await find_prime_numbers(list(range(first, last)))
    return {'prime numbers': prime_numbers}
