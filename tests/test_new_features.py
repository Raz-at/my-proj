import pytest
def add_number(a,b):
    return a+b

def test_add_numbers():
    assert add_number(2,3) == 5
    assert add_number(3,3) == 6
    assert add_number(2,-2) == -1


    