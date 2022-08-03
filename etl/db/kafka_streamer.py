"""."""

import logging
from typing import List

import config
from db.abstract_streamer import AbstractStreamer
from kafka import KafkaConsumer
from models import FilmBase, FilmView
from time import  sleep

logger = logging.getLogger(__name__)


class KafkaStreamer(AbstractStreamer):
    """."""

    consumer: dict = {}

    def __init__(self):
        """."""
        self.batch_size = config.BATCH_SIZE

    def read(self, topic: str) -> List[FilmBase]:
        """Функция чтения.

        Args:
            topic: Имя топика.

        Returns:
            - Список фильмов.
        """
        logger.info(f'Start to read {topic}')

        result_dict = []
        for m in self.__get_consumer(topic):
            result_dict.append(
                FilmView(user=m.key[5:41], film=m.key[47:], progress_time=m.value)
            )
            print(f' eto result_dict read from kafka: {result_dict}')
            if len(result_dict) >= self.batch_size:
                break

        logger.info(f'Close {topic} consumer')
        return result_dict

    def __get_consumer(self, topic: str) -> consumer:
        """Get consumer.

        Args:
            topic: Имя топика.

        Returns:
            consumer
        """
        if topic not in self.consumer:
            self.consumer[topic] = KafkaConsumer(topic, **self.__get_consumer_params())
        return self.consumer[topic]

    def __get_consumer_params(self) -> dict:
        """.

        Returns:
            dict
        """
        return {
            'bootstrap_servers': [f'{config.KAFKA_HOST}:{config.KAFKA_PORT}'],
            'auto_offset_reset': 'earliest',
            'group_id': 'echo-messages-to-stdout',
            'consumer_timeout_ms': config.CONSUMER_TIMEOUT_MS,
        }

if __name__ == '__main__':
    try:
        reader = KafkaStreamer(
        )
        while True:
            reader.read()
        time.sleep(2)

    except KeyboardInterrupt:
        logger.info('Program is stopped')