from src.math_operation import Add, Sub

def test_add():
    assert Add(2,3) == 5
    assert Add(-1,-1) == -2
    assert Add(10,0) == 10

def test_sub():
    assert Sub(5,5) == 0
    assert Sub(5,3) == 2
    assert Sub(-5,-5) == -10