from hashlib import sha256


def hash(filepath: str) -> str:
    with open(filepath, 'rb') as file:
        bytes = file.read()
        return sha256(bytes).hexdigest()


def assert_hash_eq(filepath: str, expected: str):
    actual = hash(filepath)
    if actual != expected:
        raise AssertionError(
            f'Expected file \'{filepath}\' hash to be {expected}, '
            f'got {actual}'
        )


if __name__ == '__main__':
    for filepath, expected_hash in (
        ('user/alloctest.c', 'aeae25efad41d8d7853e5117eea1a8b46b60197d8fec55bc48891f841b25e1ea'),
        ('user/cowtest.c', 'e8b30f01ce2ee128efa61124a6462caece54ff4c29c7298d914ae00899a2648c'),
        ('user/dump2tests.c', '6777b20db37fa8025217fd7c1002dd81e16e38f71168cf34a44d237de5caff98'),
        ('user/dumptests.c', 'aa5d9415433df40f5d78e9a17231b6b5977a56eff057db1d0f03535126b19c60'),
        ('user/forktest.c', 'b5f9c6a9e6ebfbd3907be1887942a972195863589f6a83d42bcb7ea4296d11ad'),
        ('user/lazytests.c', '565238128883ec38408f5d8c6d63b3db94e0ecb78a93afcb9a2c8ff7714362b2'),
        ('user/usertests.c', '182ed86d306a3acec493995da9ba296d153a102c632e2905b3f561838cddbe22'),
    ): 
        print(f"Checking a hash of '{filepath}'...")
        assert_hash_eq(filepath, expected_hash)
