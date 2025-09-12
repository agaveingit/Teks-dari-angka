import time
from main import Konverter

def time_function(func, n: int) -> None:
    start: float = time.perf_counter()
    result: str = func(n)
    end: float = time.perf_counter()

    print(f"{func.__name__}({n}) = {result}")
    print(f"Time result {end - start:.9f} s")

k = Konverter()
time_function(k.konversi, 999999999999)