from datetime import timedelta

from stream import RWStream
from suite.core import TestSuite, expect
from test import Test, Xv6UserTest, assert_eq
from timeout import TimeBudget
from xv6 import Xv6


QUICK_TESTS = [
    Xv6UserTest(name="copyin", timeout=timedelta(seconds=20)),
    Xv6UserTest(name="copyout", timeout=timedelta(milliseconds=200)),
    Xv6UserTest(name="copyinstr1", timeout=timedelta(milliseconds=200)),
    Xv6UserTest(name="copyinstr2", timeout=timedelta(milliseconds=200)),
    Xv6UserTest(name="copyinstr3", timeout=timedelta(milliseconds=200)),
    Xv6UserTest(name="rwsbrk", timeout=timedelta(seconds=1)),
    Xv6UserTest(name="truncate1", timeout=timedelta(seconds=2)),
    Xv6UserTest(name="truncate2", timeout=timedelta(seconds=2)),
    Xv6UserTest(name="truncate3", timeout=timedelta(seconds=8)),
    Xv6UserTest(name="openiput", timeout=timedelta(seconds=1)),
    Xv6UserTest(name="exitiput", timeout=timedelta(seconds=1)),
    Xv6UserTest(name="iput", timeout=timedelta(seconds=1)),
    Xv6UserTest(name="opentest", timeout=timedelta(seconds=1)),
    Xv6UserTest(name="writetest", timeout=timedelta(seconds=16)),
    Xv6UserTest(name="writebig", timeout=timedelta(seconds=30)),
    Xv6UserTest(name="createtest", timeout=timedelta(seconds=30)),
    Xv6UserTest(name="dirtest", timeout=timedelta(seconds=1)),
    Xv6UserTest(name="exectest", timeout=timedelta(seconds=2)),
    Xv6UserTest(name="pipe1", timeout=timedelta(milliseconds=500)),
    Xv6UserTest(name="killstatus", timeout=timedelta(seconds=12)),
    Xv6UserTest(
        name="preempt",
        suffix_size=len("kill... wait... "),
        timeout=timedelta(milliseconds=500),
    ),
    Xv6UserTest(name="exitwait", timeout=timedelta(seconds=1)),
    Xv6UserTest(name="reparent", timeout=timedelta(seconds=3)),
    Xv6UserTest(name="twochildren", timeout=timedelta(seconds=10)),
    Xv6UserTest(name="forkfork", timeout=timedelta(seconds=3)),
    Xv6UserTest(name="forkforkfork", timeout=timedelta(seconds=8)),
    Xv6UserTest(name="reparent2", timeout=timedelta(seconds=15)),
    Xv6UserTest(name="mem", timeout=timedelta(seconds=5)),
    Xv6UserTest(name="sharedfd", timeout=timedelta(seconds=36)),
    Xv6UserTest(name="fourfiles", timeout=timedelta(seconds=5)),
    Xv6UserTest(name="createdelete", timeout=timedelta(seconds=45)),
    Xv6UserTest(name="unlinkread", timeout=timedelta(seconds=2)),
    Xv6UserTest(name="linktest", timeout=timedelta(seconds=2)),
    Xv6UserTest(name="concreate", timeout=timedelta(seconds=70)),
    Xv6UserTest(name="linkunlink", timeout=timedelta(seconds=12)),
    Xv6UserTest(name="subdir", timeout=timedelta(seconds=5)),
    Xv6UserTest(name="bigwrite", timeout=timedelta(seconds=40)),
    Xv6UserTest(name="bigfile", timeout=timedelta(seconds=4)),
    Xv6UserTest(name="fourteen", timeout=timedelta(seconds=2)),
    Xv6UserTest(name="rmdot", timeout=timedelta(seconds=2)),
    Xv6UserTest(name="dirfile", timeout=timedelta(seconds=2)),
    Xv6UserTest(name="iref", timeout=timedelta(seconds=16)),
    Xv6UserTest(name="forktest", timeout=timedelta(seconds=1)),
    Xv6UserTest(name="sbrkbasic", timeout=timedelta(seconds=3)),
    Xv6UserTest(name="sbrkmuch", timeout=timedelta(seconds=2)),
    Xv6UserTest(
        name="kernmem",
        timeout=timedelta(milliseconds=500),
        suffix_size=len("usertrap(): unexpected scause 0xd pid=6452"),
        extra_lines=79,
    ),
    Xv6UserTest(
        name="MAXVAplus",
        timeout=timedelta(seconds=30),
        suffix_size=len("usertrap(): unexpected scause 0xf pid=6515"),
        extra_lines=51,
    ),
    Xv6UserTest(
        name="sbrkfail",
        timeout=timedelta(seconds=8),
        suffix_size=len("usertrap(): unexpected scause 0xd pid=6553"),
        extra_lines=1,
    ),
    Xv6UserTest(name="sbrkarg", timeout=timedelta(seconds=2)),
    Xv6UserTest(name="validatetest", timeout=timedelta(seconds=2)),
    Xv6UserTest(name="bsstest", timeout=timedelta(seconds=2)),
    Xv6UserTest(name="bigargtest", timeout=timedelta(seconds=2)),
    Xv6UserTest(name="argptest", timeout=timedelta(seconds=2)),
    Xv6UserTest(
        name="stacktest",
        timeout=timedelta(seconds=2),
        suffix_size=len("usertrap(): unexpected scause 0xd pid=6561"),
        extra_lines=1,
    ),
    Xv6UserTest(
        name="nowrite",
        timeout=timedelta(seconds=2),
        suffix_size=len("usertrap(): unexpected scause 0xf pid=6563"),
        extra_lines=11,
    ),
    Xv6UserTest(name="pgbug", timeout=timedelta(seconds=2)),
    Xv6UserTest(
        name="sbrkbugs",
        timeout=timedelta(seconds=2),
        suffix_size=len("usertrap(): unexpected scause 0xc pid=6571"),
        extra_lines=3,
    ),
    Xv6UserTest(name="sbrklast", timeout=timedelta(seconds=2)),
    Xv6UserTest(name="sbrk8000", timeout=timedelta(seconds=2)),
    Xv6UserTest(name="badarg", timeout=timedelta(seconds=6)),
]


SLOW_TESTS = [
    Xv6UserTest(name="bigdir", timeout=timedelta(seconds=120)),
    Xv6UserTest(name="manywrites", timeout=timedelta(seconds=180)),
    Xv6UserTest(name="badwrite", timeout=timedelta(seconds=200)),
    Xv6UserTest(name="execout", timeout=timedelta(seconds=40)),
    Xv6UserTest(
        name="diskfull",
        timeout=timedelta(seconds=160),
        suffix_size=len("balloc: out of blocks"),
        extra_lines=1,
    ),
    Xv6UserTest(
        name="outofinodes",
        timeout=timedelta(seconds=130),
        suffix_size=len("ialloc: no inodes"),
    ),
]


class Xv6UserTestSuite(TestSuite):
    def start(self, stream: RWStream):
        Xv6(stream).run("usertests")

    def expect(self, stream: RWStream):
        assert stream.readline().endswith("usertests starting")
        self.expect_part("quick", stream)
        self.expect_part("slow", stream)

    def expect_part(self, name: str, stream: RWStream):
        assert name in ("quick", "slow")

        match name:
            case "quick":
                tests = QUICK_TESTS
            case "slow":
                tests = SLOW_TESTS

        expected_duration = sum(test.timeout.total_seconds() for test in tests)
        print(f"[ 0%] Running suite '{name}'... Expected duration {expected_duration}s.")

        expect(stream, tests)

        match name:
            case "quick":
                assert_eq(stream.readline(), "usertests slow tests starting")
            case "slow":
                assert_eq(stream.readline(), "ALL TESTS PASSED")

        print(f"[OK ] Test suite '{name}' was passed!")
