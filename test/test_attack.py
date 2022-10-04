import os

import pytest

os.chdir(os.getcwd() + "/..")

from tools.method import AttackMethod

# Testing if we can make a succesfull attack (only HTTP by now)
methods = ["HTTP"]


@pytest.mark.parametrize("method", methods)
def test_Start(method):

    with AttackMethod("HTTP", 5, 10, "google.com") as attack:
        assert attack.Start() == True
