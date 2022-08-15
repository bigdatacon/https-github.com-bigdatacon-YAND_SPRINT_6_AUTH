
from kafka import KafkaProducer
from time import sleep
import logging
from logging import config as logger_conf
from log_config import LOGGING
from pythonjsonlogger import jsonlogger
from config.config import Config
from gen_functions import generate_event_value, generate_uuid
import random
from time import sleep
from my_backoff import backoff

logger_conf.dictConfig(LOGGING)
logger = logging.getLogger(__name__)

logger.info('Start SEND_MSG')

config = Config.parse_file('config/config.json')

topics = config.common.topics
users = [generate_uuid() for _ in range(config.writer.users_count)]
films = [generate_uuid() for _ in range(config.writer.films_count)]

class KafkaWriter:
    """Класс описывающий функции для записи данныз в kafka."""

    def __init__(
        self,
        topics_names: list,
        host: str,
        port: int,
        sleeping_time: float,
        max_comment_len: int,
    ):
        """
        Функция инициализации экземпляра класса.
        Args:
            topics_names: Имена топиков.
            host: Хост kafka.
            port: Порт kafka.
            sleeping_time: Частота занесения данных.
            max_comment_len: Максимальная длина комментария.
        """
        self.topics = topics_names
        self.host = host
        self.port = port
        self.producer = self.connect()
        self.event_key = None
        self.event_type = None
        self.event_value = None
        self.sleeping_time = sleeping_time
        self.max_comment_len = max_comment_len

    @backoff()
    def connect(self) -> KafkaProducer:
        """
        Функция подключения к Kafka.
        Returns:
            KafkaProducer: подключение
        """
        return KafkaProducer(bootstrap_servers=[f'{self.host}:{self.port}'])

    def send(self) -> None:
        """
        Функция отправки сообщений в kafka.
        Return:
            None
        """
        self.producer.send(
            topic=self.event_type,
            key=self.event_key.encode(),
            value=self.event_value.encode(),
        )
        sleep(self.sleeping_time)

    def gen_row(self) -> None:
        """Функция генерации случайных значений для занесения в kafka."""
        user_id = users[random.randrange(len(users))]
        film_id = films[random.randrange(len(films))]

        self.event_key = f'user_{user_id}_film_{film_id}'
        self.event_type = topics[random.randrange(len(topics))]
        self.event_value = generate_event_value(self.event_type, self.max_comment_len)

        logger.info(
            f"Send to '{self.event_type}' - '{self.event_key}': '{self.event_value}'"
        )

    def clear(self) -> None:
        """Функция очистки используемых переменны."""
        self.event_key = None
        self.event_type = None
        self.event_value = None

    def run(self) -> None:
        """Функция запуска."""
        self.gen_row()
        self.send()
        self.clear()


if __name__ == '__main__':
    try:
        writer = KafkaWriter(
            config.common.topics,
            config.kafka.host,
            config.kafka.port,
            config.writer.speed,
            config.writer.max_comment_len,
        )
        while True:
            writer.run()
            sleep(config.writer.speed)
    except KeyboardInterrupt:
        logger.info('Program is stopped')