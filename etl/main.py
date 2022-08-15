"""."""

import logging
import time
from datetime import datetime
from logging import config as logger_conf

import config
from db.ch_storage import CHStorage
from db.kafka_streamer import KafkaStreamer
from log_config import LOGGING
from sts import StreamerToStorage

logger_conf.dictConfig(LOGGING)
logger = logging.getLogger(__name__)


def do_etl():
    """Docstring."""
    logger.info('Start ETL')
    etl = StreamerToStorage(streamer=KafkaStreamer(), storage=CHStorage())

    try:
        while True:
            logger.info('New sync round started at {0}'.format(datetime.now()))
            etl.sync()
            time.sleep(config.SLEEP_TIME)
    except KeyboardInterrupt:
        logger.info('Program is stopped')


if __name__ == '__main__':
    do_etl()
