import pytest
from apptest import add, subtract

def test_add():
    assert add(2, 2) == 4

def test_subtract():
    assert subtract(2, 1) == 1