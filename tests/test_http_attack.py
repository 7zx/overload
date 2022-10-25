import os

import pytest

os.chdir(os.getcwd() + "/..")

from tools.method import AttackMethod  # type: ignore[import]

use_proxy = [True, False]


@pytest.mark.parametrize("use_proxy", use_proxy)
def test_start(use_proxy: bool) -> None:

    with AttackMethod("HTTP", 10, 10, "google.com", use_proxy) as attack:
        assert attack.start() == True
