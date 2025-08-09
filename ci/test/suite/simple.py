from timeout import TimeBudget
from suite.core import TestSuite, expect
from test import Test, assert_eq, assert_matches
from stream import RWStream
from xv6 import Xv6


class SimpleSuite(TestSuite):
    def __init__(self, name: str, prologue: list[str], tests: list[Test], epilogue: list[str]):
        self.name = name
        self.prologue = prologue
        self.tests = tests
        self.epilogue = epilogue

        if len(self.prologue) != 0:
            self.prologue[0] = f"(\\$ )+{self.prologue[0]}"
        else:
            self.tests[0].patterns[0] = f"(\\$ )+{self.tests[0].patterns[0]}"

    def start(self, stream: RWStream):
        Xv6(stream).run(self.name)

    def expect(self, stream: RWStream):
        self._expect(stream, self.prologue)
        expect(stream, self.tests)
        self._expect(stream, self.epilogue)

    def _expect(self, stream: RWStream, patterns: list[str]):
        for pattern in patterns:
            assert_matches(stream.readline(), pattern)
