import logging

from classification.config import config
from classification.config import logging_config

VERSION_PATH = config.PACKAGE_ROOT / 'VERSION'


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging_config.get_console_handler())
logger.propagate = False

with open(VERSION_PATH, 'r') as version_path:
    __version__ = version_path.read().strip()