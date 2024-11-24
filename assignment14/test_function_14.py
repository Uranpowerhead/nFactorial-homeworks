from function_14 import multiply

def test_multiply():
    assert multiply(5, 6) == 30
    assert multiply(0, 1) == 0
    assert multiply(-10, 1) == -10
    assert multiply(-5, -5) == 25
    assert multiply(-5, 0) == 0
    assert multiply(20, 10) == 200