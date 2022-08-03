"""Валидация конфигурационного файла."""

from pydantic import BaseModel


class KafkaSettings(BaseModel):
    """Настройки kafka."""

    host: str
    port: int


class ClickHouseSettings(BaseModel):
    """Настройки ClickHouse."""

    host: str
    port: int


class CommonSettings(BaseModel):
    """Основные настройки."""

    topics: list


class ReaderSettings(BaseModel):
    """Настройки считывателя из kafka."""

    consumer_timeout_ms: float
    sleeping_time: float


class WriterSettings(BaseModel):
    """Настройки писателя в kafka."""

    users_count: int
    films_count: int
    speed: float
    max_comment_len: int


class Config(BaseModel):
    """Файл конфигурации."""

    kafka: KafkaSettings
    clickhouse: ClickHouseSettings
    common: CommonSettings
    reader: ReaderSettings
    writer: WriterSettings
