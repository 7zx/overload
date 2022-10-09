import os

import pytest

os.chdir(os.getcwd() + "/..")

from tools.method import AttackMethod

# Testing if we can make a successful attack (only HTTP by now)
methods = ["HTTP"]


@pytest.mark.parametrize("method", methods)
def test_Start(method: str) -> None:

    with AttackMethod(method, 5, 10, "google.com") as attack:
        assert attack.start() == True
