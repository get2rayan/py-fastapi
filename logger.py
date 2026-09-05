import logging
from logging import Logger
import os
import sys

from dotenv import load_dotenv

load_dotenv()

logger: Logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG if (
            os.getenv('DEBUG_MODE','').lower() in ['true', '1', 'yes'] or 
            sys.stdout.isatty()
            ) else logging.INFO)
logger.handlers.clear()
logger.propagate = False

 # Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Create console handler and set level to debug
ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(ch)
