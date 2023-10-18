from functions import add, subtract, multiply, divide

def calculator_if(value1, value2, operation):
    if operation == '+':
        return add(value1, value2)
    elif operation == '-':
        return subtract(value1, value2)
    elif operation == '*':
        return multiply(value1, value2)
    elif operation == '/':
        return divide(value1, value2)
    else:
        return "Error: Invalid operation"