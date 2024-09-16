from math import ceil
from abc import ABC, abstractmethod
from enum import Enum

from test import Test, Xv6UserTest, assert_eq
from timeout import TimeBudget
from stream import RWStream


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


class TestSuite(ABC):
    @abstractmethod
    def start(self, stream: RWStream):
        pass

    @abstractmethod
    def expect(self, stream: RWStream):
        pass
