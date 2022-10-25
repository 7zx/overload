import os

import pytest

os.chdir(os.getcwd() + "/..")

from tools.method import AttackMethod  # type: ignore[import]

use_proxy = [False]


@pytest.mark.parametrize("use_proxy", use_proxy)
def test_start(use_proxy: bool) -> None:

    with AttackMethod("SlowLoris", 10, 10, "google.com", use_proxy, 3) as attack:
        assert attack.start() == True
