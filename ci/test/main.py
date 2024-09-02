import re
from math import ceil
from typing import NamedTuple
from datetime import timedelta, datetime

from registry import QUICK_TESTS
from qemu import Qemu
from test import Test
from timeout import TimeBudget


class TestResult(NamedTuple):
    duration: timedelta


def assert_eq(lhs, rhs):
    if lhs != rhs:
        print(f"Assertion failed: '{lhs}' != '{rhs}'")
    assert lhs == rhs


def read_header(qemu: Qemu):
    prefix = [qemu.readline() for _ in range(7)]
    assert_eq(prefix[2], "xv6 kernel is booting")
    assert_eq(prefix[3], "")
    assert prefix[4] in (f"hart {i + 1} starting" for i in range(2))
    assert prefix[5] in (f"hart {i + 1} starting" for i in range(2))
    assert_eq(prefix[6], "init: starting sh")


def start_usertests(qemu: Qemu):
    qemu.writeline("usertests")
    assert_eq(qemu.readline(), "usertests")
    assert_eq(qemu.readline(), "")
    assert_eq(qemu.readline(), "$ usertests starting")


def read_test(qemu: Qemu, test: Test) -> TestResult:
    pattern = "test " + test.name + ": .{" + str(test.suffix_size) + "}"
    if test.extra_lines == 0:
        pattern += "OK"

    begin = datetime.now()

    status = qemu.readline()
    if not re.fullmatch(pattern, status):
        raise ValueError(f"Unexpected {status = }")

    for i in range(test.extra_lines):
        qemu.readline()

    if test.extra_lines != 0:
        status = qemu.readline()
        if status != "OK":
            raise ValueError(f"Unexpected {status = }")

    end = datetime.now()
    
    return TestResult(
        duration=end - begin,
    )


if __name__ == "__main__":
    print("Starting Xv6 userspace tests...")

    with Qemu(cwd="../..") as qemu:
        print("Qemu was started.")

        read_header(qemu)
        print("Kernel was booted.")

        start_usertests(qemu)

        current_duration = 0
        total_duration = sum(test.timeout.total_seconds() for test in QUICK_TESTS)
        for test in QUICK_TESTS:
            expected_duration = test.timeout.total_seconds()
            progress = round(current_duration / total_duration * 100)

            print(f"[{str(progress).rjust(2)}%] Running test '{test.name}'...".ljust(36), end=" ", flush=True)
            print(f"{expected_duration:.3f}s".rjust(7), end=" > ", flush=True)

            with TimeBudget(ceil(test.timeout.total_seconds())):
                result = read_test(qemu, test)

            print(f"{result.duration.total_seconds():.3f}s".rjust(7), "=> OK!")

            current_duration += expected_duration
        
        print("Quick tests passed!")
