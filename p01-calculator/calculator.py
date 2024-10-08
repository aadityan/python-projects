def add(a, b):
    return a + b

def substract(a, b):
    return a - b 

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by 0")
    return a / b

def calc(operator, a, b):

    operators = {
        '+': add,
        '-': substract,
        '*': multiply,
        '/': divide
    }

    if operator not in operators:
        raise ValueError(f"Invalid operation: {operator}")
    
    return operators[operator](a, b)