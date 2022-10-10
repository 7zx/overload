import os

import pytest

os.chdir(os.getcwd() + "/..")

from tools.method import AttackMethod  # type: ignore[import]

# Testing if we can make a successful attack (only HTTP by now)
methods = ["HTTP"]
use_proxy = [True, False]


@pytest.mark.parametrize("method", methods)
@pytest.mark.parametrize("use_proxy", use_proxy)
def test_start(method: str, use_proxy: bool) -> None:

    with AttackMethod(method, 10, 10, "google.com", use_proxy) as attack:
        assert attack.start() == True
