import signal
from datetime import timedelta


class TimeoutException(Exception):
    pass


class TimeBudget:
    def __init__(self, seconds: int, message=None):
        self.seconds = seconds
        self.message = (
            message if message is not None else f"Operation timed out {self.seconds}s"
        )

    def __enter__(self):
        signal.signal(signal.SIGALRM, self._timeout_handler)
        signal.alarm(self.seconds)

    def __exit__(self, exc_type, exc_value, traceback):
        signal.alarm(0)

    def _timeout_handler(self, signum, frame):
        raise TimeoutException(self.message)
