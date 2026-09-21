from main import *

# 2 pts

def test_simple_work():
    assert simple_work_calc(8, 2, 2) == 32
    assert simple_work_calc(8, 3, 2) == 65
    assert simple_work_calc(9, 2, 3) == 19


# 2 pts

def test_work():
    assert work_calc(8, 2, 2, lambda n: n) == 32
    assert work_calc(8, 1, 2, lambda n: n*n) == 85
    assert work_calc(8, 3, 2, lambda n: 1) == 40


# 2 pts

def test_span():
    assert span_calc(10, 2, 2, lambda n: 1) == 4
    assert span_calc(20, 1, 4, lambda n: n*n) == 426
    assert span_calc(30, 3, 4, lambda n: n) == 38