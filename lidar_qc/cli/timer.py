import time
from datetime import datetime, timedelta

from lidar_qc.log import get_logger

logger = get_logger()


def start_timer() -> float:
    """
    Starting timer for script processing time and logging the start time information.
    Returns the time the perf_counter was started, in fractional seconds.
    """
    start_time = time.perf_counter()
    logger.info(f"Script Started: {datetime.now()}")
    return start_time


def end_timer(start_time) -> None:
    """
    Logger statement for the time when script processing finished and the time duration of the script.
    """
    logger.info(f"Script Finished: {datetime.now()} in {timedelta(seconds=time.perf_counter() - start_time)}")
