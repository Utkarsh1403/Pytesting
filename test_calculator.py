import Calculator


def test_Add():
    x = 10
    y = 25
    result= Calculator.addition(x,y)
    assert x+y==result

def test_sub():
    x = 10
    y = 20
    result = Calculator.substraction(x,y)
    assert x-y==result

def test_multi():
    x = 10
    y = 20
    result = Calculator.multiply(x,y)
    assert x*y == result
def test_div():
    x = 10
    y = 20
    result = Calculator.divide(x,y)
    assert x/y== result


