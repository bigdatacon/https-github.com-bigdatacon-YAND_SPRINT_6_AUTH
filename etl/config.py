"""."""

import os
SLEEP_TIME = int(os.getenv('SLEEP_TIME', 3))
TOPICS = os.getenv('TOPICS', 'views').split(',')
KAFKA_HOST = os.getenv('KAFKA_HOST', 'localhost')
KAFKA_PORT = int(os.getenv('KAFKA_PORT', 9092))
CH_HOST = os.getenv('CH_HOST', 'localhost')
CONSUMER_TIMEOUT_MS = int(os.getenv('CONSUMER_TIMEOUT_MS', 10000))
BATCH_SIZE = int(os.getenv('BATCH_SIZE', 5))


