import pytest
from myfile import divide

def test_divide_pass():
    assert divide(10,2) == 5

def test_divide_fail():
    assert divide(5,1) == 5