from kafka import KafkaConsumer
import logging
from logging import config as logger_conf
from log_config import LOGGING
from pythonjsonlogger import jsonlogger

logger_conf.dictConfig(LOGGING)
logger = logging.getLogger(__name__)

logger.info('Start READ_MSG')
consumer = KafkaConsumer(
    'views',
    # 'test_topic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    group_id='echo-messages-to-stdout',
)

for message in consumer:
    print(message, message.value)

# ConsumerRecord(topic='views', partition=0, offset=34, timestamp=1659483816583, timestamp_type=0, key=b'user_d17df40f-f89c-4a3c-8d75-cb52d4fbf02b_film_a9bc7335-1608-4aa0-a7cc-f12f4f16e5b0', value=b'119', headers=[], checksum=None, serialized_key_size=83, serialized_value_size=3, serialized_header_size=-1) b'119'