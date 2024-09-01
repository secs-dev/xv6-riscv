from datetime import timedelta
from typing import NamedTuple


class Test(NamedTuple):
    name: str
    timeout: timedelta
    suffix_size: int = 0
    extra_lines: int = 0
