from datetime import timedelta

from test import PatternTest
from suite.simple import SimpleSuite


DUMPTESTS = SimpleSuite(
    name = "dumptests",
    prologue = [
        "dump tests started",
        "dump syscall found. Start testing",
    ],
    tests = [
        PatternTest(
            name = "0",
            timeout = timedelta(seconds = 1),
            patterns = [
                "#####################",
                "#                   #",
                "#   initial state   #",
                "#                   #",
                "#####################",
                "s2 = \\d+",
                "s3 = \\d+",
                "s4 = \\d+",
                "s5 = \\d+",
                "s6 = \\d+",
                "s7 = \\d+",
                "s8 = \\d+",
                "s9 = \\d+",
                "s10 = \\d+",
                "s11 = \\d+",
            ],
        ),
        PatternTest(
            name = "1",
            timeout = timedelta(seconds = 1),
            patterns = [
                "#####################",
                "#                   #",
                "#       test 1      #",
                "#                   #",
                "#####################",
                "#                   #",
                "#  expected values  #",
                "#                   #",
                "#####################",
                "# s2  = 2           #",
                "# s3  = 3           #",
                "# s4  = 4           #",
                "# s5  = 5           #",
                "# s6  = 6           #",
                "# s7  = 7           #",
                "# s8  = 8           #",
                "# s9  = 9           #",
                "# s10 = 10          #",
                "# s11 = 11          #",
                "#####################",
                "s2 = 2",
                "s3 = 3",
                "s4 = 4",
                "s5 = 5",
                "s6 = 6",
                "s7 = 7",
                "s8 = 8",
                "s9 = 9",
                "s10 = 10",
                "s11 = 11",
            ],
        ),
        PatternTest(
            name = "2",
            timeout = timedelta(seconds = 1),
            patterns = [
                "#####################",
                "#                   #",
                "#      test 2       #",
                "#                   #",
                "#####################",
                "#                   #",
                "#  expected values  #",
                "#                   #",
                "#####################",
                "# s2 = 1            #",
                "# s3 = -12          #",
                "# s4 = 123          #",
                "# s5 = -1234        #",
                "# s6 = 12345        #",
                "# s7 = -123456      #",
                "# s8 = 1234567      #",
                "# s9 = -12345678    #",
                "# s10 = 123456789   #",
                "# s11 = -1234567890 #",
                "#####################",
                "s2 = 1",
                "s3 = -12",
                "s4 = 123",
                "s5 = -1234",
                "s6 = 12345",
                "s7 = -123456",
                "s8 = 1234567",
                "s9 = -12345678",
                "s10 = 123456789",
                "s11 = -1234567890",
            ],
        ),
        PatternTest(
            name = "3",
            timeout = timedelta(seconds = 1),
            patterns = [
                "#####################",
                "#                   #",
                "#      test 3       #",
                "#                   #",
                "#####################",
                "#                   #",
                "#  expected values  #",
                "#                   #",
                "#####################",
                "# s2 = 2147483647   #",
                "# s3 = -2147483648  #",
                "# s4 = 1337         #",
                "# s5 = 2020         #",
                "# s6 = 3234         #",
                "# s7 = 3235         #",
                "# s8 = 3236         #",
                "# s9 = 3237         #",
                "# s10 = 3238        #",
                "# s11 = 3239        #",
                "#####################",
                "s2 = 2147483647",
                "s3 = -2147483648",
                "s4 = 1337",
                "s5 = 2020",
                "s6 = 3234",
                "s7 = 3235",
                "s8 = 3236",
                "s9 = 3237",
                "s10 = 3238",
                "s11 = 3239",
                
            ],
        ),
    ],
    epilogue = [
        "4 tests were ran",
    ],
)


DUMP2TESTS = SimpleSuite(
    name = "dump2tests",
    prologue = [
        "dump2 tests started",
        "dump2 syscall found. Start testing",
    ],
    tests = [
        PatternTest(
            name = "1",
            timeout = timedelta(seconds = 1),
            patterns = [
                "test 1 started",
                "\\[SUCCESS\\] test 1 passed",
                "test 1 finished",
            ],
        ),
        PatternTest(
            name = "2",
            timeout = timedelta(seconds = 1),
            patterns = [
                "test 2 started",
                "\\[SUCCESS\\] test 2 passed",
                "test 2 finished",
            ],
        ),
        PatternTest(
            name = "3",
            timeout = timedelta(seconds = 1),
            patterns = [
                "test 3 started",
                "\\[SUCCESS\\] test 3 passed",
                "test 3 finished",
            ],
        ),
        PatternTest(
            name = "4",
            timeout = timedelta(seconds = 1),
            patterns = [
                "test 4 started",
                "\\[INFO\\] testing nonexisting proccess",
                "\\[OK\\] nonexisting proccess",
                "\\[INFO\\] testing illegal access to registers",
                "\\[OK\\] illegal access to registers",
                "\\[INFO\\] testing incorrect number of register",
                "\\[OK\\] incorrect number of register",
                "\\[INFO\\] testing invalid memory address",
                "\\[OK\\] invalid memory address",
                "\\[SUCCESS\\] test 4 passed",
                "test 4 finished",        
            ],
        ),
    ],
    epilogue = [
        "4 tests were run. 4 tests passed",
    ]
)


ALLOCTEST = SimpleSuite(
    name = "alloctest",
    prologue = [],
    tests = [
        PatternTest(
            name = "filetest",
            timeout = timedelta(seconds = 2),
            patterns = [
                "filetest: start",
                "filetest: OK",
            ],
        ),
        PatternTest(
            name = "memtest",
            timeout = timedelta(seconds = 16),
            patterns = [
                "memtest: start",
                "memtest: OK",
            ],
        ),
    ],
    epilogue = [],
)


COWTEST = SimpleSuite(
    name = "cowtest",
    prologue = [],
    tests = [
        PatternTest(
            name = "simple 1",
            timeout = timedelta(seconds = 60),
            patterns = ["simple: ok"],
        ),
        PatternTest(
            name = "simple 2",
            timeout = timedelta(seconds = 60),
            patterns = ["simple: ok"],
        ),
        PatternTest(
            name = "three 1",
            timeout = timedelta(seconds = 60),
            patterns = ["three: ok"],
        ),
        PatternTest(
            name = "three 2",
            timeout = timedelta(seconds = 60),
            patterns = ["three: ok"],
        ),
        PatternTest(
            name = "three 3",
            timeout = timedelta(seconds = 60),
            patterns = ["three: ok"],
        ),
        PatternTest(
            name = "file",
            timeout = timedelta(seconds = 60),
            patterns = ["file: ok"],
        ),
    ],
    epilogue = ["ALL COW TESTS PASSED"],
)


LAZYTESTS = SimpleSuite(
    name = "lazytests",
    prologue = ["lazytests starting"],
    tests = [
        PatternTest(
            name = test_name,
            timeout = timedelta(seconds = 60),
            patterns = [
                f"running test {test_name}",
                f"test {test_name}: OK",
            ],
        ) for test_name in (
            "lazy alloc",
            "lazy unmap",
            "out of memory",
        )
    ],
    epilogue = ["ALL TESTS PASSED"],
)
