"""."""

from abc import ABC, abstractmethod
from typing import List

from models import FilmBase


class AbstractStorage(ABC):
    """."""

    @abstractmethod
    def save(self, records: List[FilmBase], topic: str):
        """Функция сохранения.

        Args:
            records: Записи.
            topic: Имя топика.

        Returns:
            None.
        """
        pass
