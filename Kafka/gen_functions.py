"""."""

import random
import string
import uuid
from typing import Optional


def generate_uuid() -> uuid:
    """Функция генерации идентификатора в формате uuid.

    Returns:
        uuid.
    """
    return uuid.uuid4()


def generate_random_string(length: int) -> str:
    """Функция генерации случайной строки.

    Args:
        length: Длина строки.

    Returns:
        Случайная строка заданной длины.
    """
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for _ in range(length))
    return rand_string


def generate_event_value(event_type: str, max_comment_len: int) -> Optional[str]:
    """Функция генерации значения события в зависимости от типа события.

    Args:
        event_type: Тип события.
        max_comment_len: Максимальная длина комметария.

    Returns:
        Значение события.
    """
    event_value = None
    if event_type == 'likes':
        event_value = str(random.randrange(10))
    elif event_type == 'comments':
        comment_len = int(random.randrange(max_comment_len))
        event_value = generate_random_string(comment_len)
    elif event_type == 'views':
        event_value = str(random.randrange(160))
    elif event_type == 'bookmarks':
        event_value = str(random.randrange(1))
    return event_value
