import logging
from pathlib import Path
from typing import Optional

LOGGER_NAME = "linz-lidar-qc"


def get_logger() -> logging.Logger:
    return logging.getLogger(LOGGER_NAME)


def configure_logging(verbose: bool = False, log_file: Optional[Path] = None) -> logging.Logger:
    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(logging.DEBUG)
    log_formatter = logging.Formatter(fmt="{asctime} {levelname:8} {message}", datefmt="%Y-%m-%d %H:%M:%S", style="{")
    if log_file is not None:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(log_formatter)
        if verbose is True:
            file_handler.setLevel(logging.DEBUG)
        else:
            file_handler.setLevel(logging.INFO)
        logger.addHandler(file_handler)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(log_formatter)
    if verbose is True:
        stream_handler.setLevel(logging.DEBUG)
    else:
        stream_handler.setLevel(logging.INFO)
    logger.addHandler(stream_handler)
    return logger
