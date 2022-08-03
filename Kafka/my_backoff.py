"""."""

import logging
from functools import wraps
from time import sleep
from typing import Any, Callable

logger = logging.getLogger('__name__')


def backoff(
        start_sleep_time: float = 0.1,
        factor: int = 2,
        border_sleep_time: int = 10
) -> Callable:
    """
    Функция для повторного выполнения функции через некоторое время, если возникла ошибка.

    Args:
        start_sleep_time: начальное время повтора
        factor: во сколько раз нужно увеличить время ожидания
        border_sleep_time: граничное время ожидания

    Returns:
        результат выполнения функции
    """

    def func_wrapper(func: Any) -> Any:
        @wraps(func)
        def inner(*args, **kwargs):
            t: float = start_sleep_time
            while True:
                try:
                    connection = func(*args, **kwargs)
                    return connection
                except Exception:
                    if t >= border_sleep_time:
                        t = border_sleep_time
                    else:
                        t += start_sleep_time * 2 ** factor
                    logger.info(f'Unable to connect, backing off fot {t} seconds.')
                    sleep(t)

        return inner

    return func_wrapper
