from main import *

# 2 pts
def test_simple_work():
	assert simple_work_calc(8, 2, 2) == 32
	assert simple_work_calc(8, 3, 2) == 1  #TODO
	assert simple_work_calc(9, 2, 3) == 1 #TODO

# 2 pts
def test_work():
	assert work_calc(8, 2, 2,lambda n: n) == 32
	assert work_calc(8, 1, 2, lambda n: n*n) == 1 #TODO
	assert work_calc(8, 3, 2, lambda n: 1) == 1 #TODO

# 2 pts
def test_span():
	assert span_calc(10, 2, 2, lambda n: 1) == 4
	assert span_calc(20, 1, 4, lambda n: n*n) == 1 #TODO
	assert span_calc(30, 3, 4, lambda n: n) == 1 #TODO
