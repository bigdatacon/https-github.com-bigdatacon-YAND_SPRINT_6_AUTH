"""."""

from abc import ABC, abstractmethod
from typing import List

from models import FilmBase


class AbstractStreamer(ABC):
    """AbstractStreamer."""

    @abstractmethod
    def read(self, topic: str) -> List[FilmBase]:
        """Функция чтения.

        Args:
            topic: Имя топика.

        Returns:
            Список фильмов.
        """
        pass
