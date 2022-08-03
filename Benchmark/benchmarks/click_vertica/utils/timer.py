"""."""

import time
from functools import wraps


def timer(iterations: int):
    """Таймер.

    Args:
        iterations: Итерации.

    Returns:
        декоратор.
    """
    def decorator(fn):
        """Декоратор.

        Args:
            fn: Фуекция.

        Returns:
            Функция.
        """
        @wraps(fn)
        def inner(*args, **kwargs):
            """Внутренняя функция.

            Args:
                args: Аргументы.
                kwargs: Аргументы.
            """
            run_times = []
            for _ in range(iterations):
                start_time = time.perf_counter()
                fn(*args, **kwargs)
                end_time = time.perf_counter()
                run_times.append(end_time - start_time)

            avg_time = sum(run_times) / len(run_times)

            print(f'Average execution time (over {iterations} runs): {avg_time:.4f} seconds\n')

        return inner

    return decorator
