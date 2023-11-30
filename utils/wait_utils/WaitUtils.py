import time
from typing import Callable

from utils.date_and_time import TimeConstants


class WaitUtils:

    @staticmethod
    def until(action_func: Callable, expected_value: object = True,
              timeout_seconds=30,
              poll_time_seconds=1):
        start_time = time.time()
        end_time = start_time + timeout_seconds

        last_exception = None

        while True:
            current_time = time.time()
            if current_time > end_time:
                raise RuntimeError(
                    'Timeout exceeded for {} with last raised exception {}'.format(action_func, last_exception))
            try:
                assert action_func() == expected_value
                return
            except AssertionError as error:
                time.sleep(poll_time_seconds)
                last_exception = error
