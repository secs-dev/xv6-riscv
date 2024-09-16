from datetime import timedelta, datetime
from typing import NamedTuple
from abc import ABC, abstractmethod
from stream import RWStream
import re


def assert_eq(lhs, rhs):
    if lhs != rhs:
        print(f"Assertion failed: '{lhs}' != '{rhs}'")
    assert lhs == rhs


def assert_matches(text, pattern):
    if not re.fullmatch(pattern, text):
        raise ValueError(f"Unexpected {text = }, expected {pattern = }")


class TestResult(NamedTuple):
    duration: timedelta


class Test(ABC):
    def __init__(self, name: str, timeout: timedelta):
        self.name = name
        self.timeout = timeout

    @abstractmethod
    def expect(self, out: RWStream) -> TestResult:
        pass


class Xv6UserTest(Test):
    def __init__(self, name: str, timeout: timedelta, 
                       suffix_size: int = 0, extra_lines: int = 0):
        super().__init__(name, timeout)
        self.suffix_size = suffix_size
        self.extra_lines = extra_lines

    def expect(self, out: RWStream) -> TestResult:
        pattern = "test " + self.name + ": .{" + str(self.suffix_size) + "}"
        if not self.is_ok_separated():
            pattern += "OK"

        begin = datetime.now()

        status = out.readline()
        if not re.fullmatch(pattern, status):
            raise ValueError(f"Unexpected {status = }")

        for i in range(self.extra_lines):
            out.readline()

        if self.is_ok_separated():
            status = out.readline()
            if status != "OK":
                raise ValueError(f"Unexpected {status = }")

        end = datetime.now()

        return TestResult(duration=end - begin)
    
    def is_ok_separated(self) -> bool:
        return self.extra_lines != 0 or self.name == "outofinodes"


class PatternTest(Test):
    def __init__(self, name: str, timeout: timedelta, 
                       patterns: list[str]):
        super().__init__(name, timeout)
        self.patterns = patterns

    def expect(self, out: RWStream) -> TestResult:
        begin = datetime.now()
        for pattern in self.patterns:
            line = out.readline()
            assert_matches(line, pattern)
        end = datetime.now()
        return TestResult(duration=end - begin)
