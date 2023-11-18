import logging
import sys

FORMATTER = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s -' '%(funcName)s:%(lineno)d - %(message)s'
    )

def get_console_handler():
    console_hanler = logging.StreamHandler(sys.stdout)
    console_hanler.setFormatter(FORMATTER)
    return console_hanler