import Calculator
import pytest

@pytest.mark.xfail
@pytest.mark.parametrize("a,b,c",[(3,2,5),(10,12,15),(2,5,8),(7,8,15)])
def test_Add(a,b,c):

    result= Calculator.addition(a,b)
    assert c ==result

@pytest.mark.parametrize("a,b,c",[(5,2,3),(15,10,5),(25,14,15)])
def test_sub(a,b,c):
    result = Calculator.substraction(a,b)
    assert c==result

@pytest.mark.parametrize("a,b,c",[(2,3,6),(3,5,15),(7,2,15),(7,5,15)])
def test_multi(a,b,c):
    result = Calculator.multiply(a,b)
    assert c == result
@pytest.mark.parametrize("a,b,c",[(20,10,2),(15,3,5),(20,5,4),(7,5,15)])
def test_div(a,b,c):

    result = Calculator.divide(a,b)
    assert c== result


