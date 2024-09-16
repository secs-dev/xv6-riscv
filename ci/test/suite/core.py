from abc import ABC, abstractmethod
from math import ceil

from stream import RWStream
from test import Test
from timeout import TimeBudget


class TestSuite(ABC):
    @abstractmethod
    def start(self, stream: RWStream):
        pass

    @abstractmethod
    def expect(self, stream: RWStream):
        pass


def expect(stream: RWStream, tests: list[Test]):
    current_duration = 0
    total_duration = sum(test.timeout.total_seconds() for test in tests)

    for test in tests:
        expected_duration = test.timeout.total_seconds()
        progress = round(current_duration / total_duration * 100)

        print(
            f"[{str(progress).rjust(2)}%] Running test '{test.name}'...".ljust(36),
            end=" ",
            flush=True,
        )
        print(f"{expected_duration:.3f}s".rjust(7), end=" > ", flush=True)

        with TimeBudget(ceil(test.timeout.total_seconds())):
            result = test.expect(stream)

        print(f"{result.duration.total_seconds():.3f}s".rjust(7), "=> OK!")

        current_duration += expected_duration
