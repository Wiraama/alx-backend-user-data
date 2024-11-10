#!/usr/bin/env python3
""" modure tu return logging """
import re, logging, os, mysql.connector
from mysql.connector import connection
from typing import List, Tuple


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """ function """
    return re.sub(
            rf'({"|".join(fields)})=[^{separator}]+',
            lambda m: f"{m.group().split('=')[0]}={redaction}", message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields: List[str] = fields

    def format(self, record: logging.LogRecord) -> str:
        """ formatting logs records """
        original_info = super().format(record)
        return filter_datum(
                self.fields,
                self.REDACTION,
                original_info,
                self.SEPARATOR
                )


PII_FIELDS: Tuple[str, ...] = (
        "name",
        "email",
        "phone",
        "ssn",
        "password")


def get_logger() -> logging.Logger:
    """ returns logging.Logger object"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    """ creating a stream handler """
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(stream_handler)

    return logger

def get_db() -> connection.MySQLConnection:
    """rturns connector to database"""
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(
            user=username,
            password=password,
            host=host,
            database=database
            )
