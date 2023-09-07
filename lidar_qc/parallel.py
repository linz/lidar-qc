import concurrent.futures
import csv
import functools
import traceback
from collections.abc import Iterable
from pathlib import Path
from time import sleep
from typing import Any, Callable, Dict, List, NamedTuple, Tuple

from tqdm import tqdm
from tqdm.contrib.logging import logging_redirect_tqdm

from lidar_qc.log import get_logger

logger = get_logger()


def resolve_futures(futures: List[Tuple[concurrent.futures.Future, Callable, Any]]):
    """
    Generator which yields the results of supplied futures as they are completed,
    continuing until all futures have finished executing.
    """
    while len(futures) > 0:
        for n, (future, func, item) in enumerate(futures):
            if future.done():
                yield future, func, item
                futures.pop(n)
                continue
        sleep(0.1)


class ParallelErrorInfo(NamedTuple):
    item: Any
    extra_kwargs: Dict[str, Any]
    error: BaseException


def run_in_parallel(
    func: Callable, items: Iterable, extra_kwargs: Dict[str, Any], start_message: str, pbar_unit: str
) -> Tuple[List[Any], List[ParallelErrorInfo]]:
    """
    Runs a process in parallel using concurrent futures.

    Args:
        func: function that details the process to run per file.
        items: an iterable of files in a directory.
        extra_kwargs: an optional argument if more arguments are required in func. If not, input an empty Dict.
        start_message: string that is printed to terminal when processing begins.
        pbar_unit: what unit for the progress bar in terminal.

    Returns the results of each future, as a list.
    """
    results = []
    errors = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = []
        for item in items:
            future = executor.submit(func, item, **extra_kwargs)
            futures.append((future, func, item))
        logger.info(start_message)
        with logging_redirect_tqdm(loggers=[logger]):
            with tqdm(total=len(futures), unit=pbar_unit) as pbar:
                for result, func, item in resolve_futures(futures):
                    pbar.update()
                    if error := result.exception():
                        # logger.error(f"Error found while processing {item}: {error}")
                        errors.append(ParallelErrorInfo(item, extra_kwargs, error))
                    else:
                        results.append(result.result())
    return results, errors


def write_errors_csv(errors: List[ParallelErrorInfo], output_file: Path) -> None:
    with open(output_file, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=ParallelErrorInfo._fields)
        writer.writeheader()
        writer.writerows([error._asdict() for error in errors])


class ParallelError(Exception):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args)
        self.trace_ = kwargs.get("trace_")


def reraise_with_stack(func):
    """
    Decorator that formats exceptions printed in terminal for a given function.
    """

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            message = f"{err.__class__.__name__} exception found while running {func.__name__}: {err}: {''.join(traceback.format_exception(err))}"
            # trace_ = "".join(traceback.format_exception(err))
            # , trace_=trace_
            raise ParallelError(message)

    return wrapped


class FatalError(Exception):
    pass
