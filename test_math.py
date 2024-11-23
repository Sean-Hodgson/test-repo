import pytest
from myMath import add

def test_addition():
    assert add(2, 2) == 4
    assert add(1, 1) == 2
    assert add(-1, -1) == -2

