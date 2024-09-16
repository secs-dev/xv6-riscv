from datetime import timedelta, datetime
from argparse import ArgumentParser

from suite.usertests import Xv6UserTestSuite
from suite.custom import DUMPTESTS, DUMP2TESTS, ALLOCTEST, COWTEST, LAZYTESTS
from test import assert_eq
from qemu import Qemu


SUITES = {
    "usertests": Xv6UserTestSuite(),
} | {
    suite.name: suite for suite in (
        DUMPTESTS,
        DUMP2TESTS,
        ALLOCTEST,
        COWTEST,
        LAZYTESTS,
    )
}


parser = ArgumentParser(
    prog='Xv6 Tester',
    description='This program runs Xv6 tests inside Qemu',
)

parser.add_argument('suites', 
    metavar='SUITE',
    type=str,
    nargs='+',
    choices=SUITES.keys(),
    help='Test suite names to run',
)


def read_header(qemu: Qemu):
    prefix = [qemu.readline() for _ in range(7)]
    assert_eq(prefix[2], "xv6 kernel is booting")
    assert_eq(prefix[3], "")
    assert prefix[4] in (f"hart {i + 1} starting" for i in range(2))
    assert prefix[5] in (f"hart {i + 1} starting" for i in range(2))
    assert_eq(prefix[6], "init: starting sh")


if __name__ == "__main__":
    print("Starting Xv6 userspace tests...")

    args = parser.parse_args()
    suites = args.suites

    print(f"Got {suites = }")

    with Qemu(cwd="../..") as qemu:
        print("Qemu was started.")

        read_header(qemu)
        print("Kernel was booted.")

        for suite_name in suites:
            suite = SUITES[suite_name]

            print(f"[ 0%] Starting suite '{suite_name}'...")
            suite.start(qemu)

            suite.expect(qemu)
            print(f"[OK ] Suite '{suite_name}' is done!")


        print("You are cool!")
