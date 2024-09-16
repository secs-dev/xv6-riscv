from subprocess import Popen, PIPE, STDOUT
from stream import RWStream


class Qemu(RWStream):
    def __init__(self, cwd="."):
        self.__proccess = None
        self.__cwd = cwd

    def __enter__(self):
        self.__proccess = Popen(
            ("make", "qemu"),
            stdout=PIPE,
            stderr=STDOUT,
            stdin=PIPE,
            text=True,
            cwd=self.__cwd,
        )
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.__proccess is None:
            return
        self.__proccess.terminate()

    def readline(self):
        return self.__proccess.stdout.readline()[:-1]

    def writeline(self, line):
        print(f"{line}\n", file=self.__proccess.stdin, flush=True)
