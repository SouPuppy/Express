import os
import logging
from datetime import datetime

log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_filename = os.path.join(log_dir, f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename=log_filename,
                    filemode='w')

logger = logging.getLogger()

# ANSI escape codes for colors
COLOR_CODES = {
    'info': '\033[94m',     # Blue
    'debug': '\033[92m',    # Green
    'warning': '\033[93m',     # Yellow
    'error': '\033[91m',     # Red
    'critical': '\033[95m',     # Magenta

    'reset': '\033[0m'       # Reset to default color
}

def log(message="", level='info'):
    if level == 'info':
        logger.info(message)
    elif level == 'debug':
        logger.debug(message)
    elif level == 'warning':
        logger.warning(message)
    elif level == 'error':
        logger.error(message)
    elif level == 'critical':
        logger.critical(message)
    else:
        logger.info(message)

    # Use the color code for the level
    color = COLOR_CODES.get(level, COLOR_CODES['reset'])
    print(f"[{color}{level}{COLOR_CODES['reset']}]\t>  {message}")

log(f"Start logging, writing in {log_filename}")
