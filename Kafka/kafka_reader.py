from kafka import KafkaConsumer
import logging
from logging import config as logger_conf
from log_config import LOGGING
from pythonjsonlogger import jsonlogger
from config.config import Config
from time import sleep
from my_backoff import backoff


logger_conf.dictConfig(LOGGING)
logger = logging.getLogger(__name__)

logger.info('Start READ_MSG')

config = Config.parse_file('config/config.json')
topics = config.common.topics


# for topic in topics:
#
#     consumer = KafkaConsumer(
#         # 'views',
#         f'{topic}',
#         # 'test_topic',
#         bootstrap_servers=['localhost:9092'],
#         auto_offset_reset='earliest',
#         group_id='echo-messages-to-stdout',
# )
#
#     for message in consumer:
#         user = message.key[5:41]
#         film = message.key[47:]
#         progress_time = message.value
#         print(f'topic, user, film, progress_time  : {topic, user, film, progress_time}' )


class KafkaReader:
    """Класс описывающий функции чтения данных в kafka."""
    def __init__(
        self,
        topics_names: list,
        host: str,
        port: int,
        sleeping_time: float,
        max_comment_len: int,
        batch_size: int
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
        self.sleeping_time = sleeping_time
        self.batch_size = batch_size


    @backoff()
    def connect(self, topic) -> KafkaConsumer:
        """
        Функция подключения к Kafka.
        Returns:
            KafkaConsumer: подключение
        """

        connection = KafkaConsumer(
        f'{topic}',
        bootstrap_servers=[f'{self.host}:{self.port}'],
        auto_offset_reset='earliest',
        group_id='echo-messages-to-stdout',
        )
        return connection

    def read(self) -> list:
        """
        Функция чтения сообщений из kafka.
        Return:
            list
        """
        result_dict = []
        for topic in self.topics:
            consumer = self.connect( topic)
            for message in consumer:
                user = message.key[5:41]
                film = message.key[47:]
                progress_time = message.value
                result_dict.append([topic, user, film, progress_time])
                logger.info(
                    f"read from kafka {topic, user, film, progress_time}"
                )
                sleep(self.sleeping_time)
                print(f' eto len result_dict: {len(result_dict)}, eto batch_size : {self.batch_size}')
                if len(result_dict) >= self.batch_size:
                    break

            logger.info(f'Close {topic} consumer, len(result_dict) = {len(result_dict)}')
            return result_dict


if __name__ == '__main__':
    try:
        reader = KafkaReader(
            config.common.topics,
            config.kafka.host,
            config.kafka.port,
            config.writer.speed,
            config.writer.max_comment_len,
            config.reader.batch_size
        )
        while True:
            data_to_ch = reader.read()
            print(f' eto data_to_ch: {data_to_ch}')
            sleep(config.writer.speed)
    except KeyboardInterrupt:
        logger.info('Program is stopped')