import pytest, calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(5, -5) == 0

def test_subtract():
    assert calculator.substract(1, 1) == 0
    assert calculator.substract(10, 1) == 9
    assert calculator.substract(1, 10) == -9

def test_multiple():
    assert calculator.multiply(1, 1) == 1
    assert calculator.multiply(4, 2) == 8
    assert calculator.multiply(4, -2) == -8
    assert calculator.multiply(-4, -2) == 8

def test_divide():
    assert calculator.divide(1, 1) == 1
    assert calculator.divide(5, 2) == 2.5

    with pytest.raises(ValueError):
        calculator.divide(2, 0)

def test_calc():
    assert calculator.calc("+", 2, 3) == 5
    assert calculator.calc("-", 2, 3) == -1
    assert calculator.calc("*", 2, 3) == 6
    assert calculator.calc("/", 5, 2) == 2.5

    with pytest.raises(ValueError):
        calculator.calc("/", 5, 0) 
    
    with pytest.raises(ValueError):
        calculator.calc('$', 5, 1)