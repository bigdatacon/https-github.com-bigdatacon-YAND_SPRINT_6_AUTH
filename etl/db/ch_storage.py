"""."""

import logging
from typing import Any, List

import config
from clickhouse_driver import Client
from db.abstract_storage import AbstractStorage
from models import FilmBase
from resouces import backoff

logger = logging.getLogger(__name__)


class CHStorage(AbstractStorage):
    """."""

    __client = None

    def __init__(self):
        """."""
        pass

    def save(self, records: List[FilmBase], topic: str) -> None:
        """Функция сохранения.

        Args:
            records: Записи.
            topic: Имя топика.
        """
        values_str = ','.join(self.prep_row(row) for row in records)
        # TODO make abstract, to handle any topic
        query = f'INSERT INTO default.film_view (id, user, film, progress_time) VALUES {values_str}'

        logger.info(query)
        self.__exec_query(query)

    def prep_row(self, row: FilmBase) -> str:
        """Функция.

        Args:
            row: Строка.

        Returns:
            row
        """
        # TODO make abstract, to handle any topic
        return f"(generateUUIDv4(), '{row.user}', '{row.film}', {row.progress_time})"

    @backoff()
    def __exec_query(self, query: str) -> None:
        """Исполнить запрос.

        Args:
            query: Запрос.
        """
        self.__get_client().execute(query)

    def __get_client(self) -> Any:
        """Получить клиента.

        Returns:
            client
        """
        if not self.__client:
            self.__client = Client(**self.__get_db_params())
        return self.__client

    def __get_db_params(self) -> dict:
        """Получить параметры БД.

        Returns:
            dict
        """
        return {'host': config.CH_HOST}
