"""class StreamToStorage."""

import logging

import config
from db.abstract_storage import AbstractStorage
from db.abstract_streamer import AbstractStreamer

logger = logging.getLogger(__name__)


class StreamerToStorage:
    """class."""

    def __init__(self, streamer: AbstractStreamer, storage: AbstractStorage):
        """
        Функция инициализации экземпляра класса.

        Args:
            streamer: Стример.
            storage: Память.
        """
        self.topics = config.TOPICS
        self.streamer = streamer
        self.storage = storage

    def sync(self):
        """."""
        for topic in self.topics:
            result_rows = self.streamer.read(topic)
            print(f' eto result_rows : {result_rows}')
            """комментирую пока нет топиков в кликхаус"""
            if result_rows:
                self.storage.save(result_rows, topic)
