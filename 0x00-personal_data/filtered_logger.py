#!/usr/bin/env python3
""" modure tu return logging """
import re
from typing import List
import logging


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
        return filter_datum(self.fields, self.REDACTION, original_info, self.SEPARATOR)
