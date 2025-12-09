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
        escaped_name = re.escape(self.name)
        pattern_inline = rf"test {escaped_name}: .*OK\s*$"
        pattern_start = rf"test {escaped_name}: .*"

        begin = datetime.now()
        first = out.readline()
        if first is None:
            raise ValueError("Unexpected EOF while waiting for test status")
        first_stripped = first.rstrip("\r\n")

        if re.fullmatch(pattern_inline, first_stripped):
            end = datetime.now()
            return TestResult(duration=end - begin)

        if not re.fullmatch(pattern_start, first_stripped):
            raise ValueError(f"Unexpected {first = }")

        debug_lines = []
        status = None

        while True:
            line = out.readline()
            if line is None:
                raise ValueError("Unexpected EOF while waiting for OK/FAILED")
            token = line.strip()
            if token == "OK" or token == "FAILED":
                status = token
                break
            debug_lines.append(line.rstrip("\r\n"))

        if status != "OK":
            if debug_lines:
                print(*debug_lines, sep="\n")
            raise ValueError(f"Unexpected {status = }, expected OK")

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
