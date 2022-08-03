"""."""

import logging
import time
from functools import wraps

logger = logging.getLogger(__name__)


def backoff(
        start_sleep_time: float = 0.1,
        factor: float = 2,
        border_sleep_time: float = 10
):
    """Функция для повторного выполнения функции через некоторое время.

    Args:
        start_sleep_time: начальное время повтора.
        factor: во сколько раз нужно увеличить время ожидания.
        border_sleep_time: граничное время ожидания.

    Returns:
        результат выполнения функции.
    """

    def func_wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            t = start_sleep_time
            while True:
                try:
                    res = func(*args, **kwargs)
                    if t != start_sleep_time:
                        logger.debug(f'Backoff for {func.__name__} successful!')
                    return res
                except Exception:
                    logger.exception('Backoff exception')
                time.sleep(t)
                t = border_sleep_time if t > border_sleep_time / 2 else t * factor

        return inner

    return func_wrapper
