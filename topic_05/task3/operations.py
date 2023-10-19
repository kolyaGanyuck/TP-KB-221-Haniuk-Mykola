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
            raise ValueError("Invalid operation")
def genIntValue(prompt: str):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Value is not an integer") 
def get_operation():
    while True:
        try:
            operation = input("Enter the operation (+, -, *, /): ")
            if operation in ('+', '-', '*', '/'):
                return operation
            else:
                raise ValueError("Invalid operation")
        except (ValueError, ZeroDivisionError) as e:
            print(f"Mistake: {e}")