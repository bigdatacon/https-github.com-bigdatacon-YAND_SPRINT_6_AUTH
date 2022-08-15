from kafka import KafkaProducer
from time import sleep
import logging
from logging import config as logger_conf
from log_config import LOGGING
from pythonjsonlogger import jsonlogger

logger_conf.dictConfig(LOGGING)
logger = logging.getLogger(__name__)

logger.info('Start SEND_MSG')
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

producer.send(
    # topic='views',
    topic='test_topic',
    value=b'1611039931',
    key=b'500271+tt0120338',
)

sleep(1)
print('send')