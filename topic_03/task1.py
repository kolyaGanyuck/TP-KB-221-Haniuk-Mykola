def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

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

while True:
    # Input values and operation from the user
    value1 = float(input("Enter the first value: "))
    value2 = float(input("Enter the second value: "))
    operation = input("Enter the operation (+, -, *, /): ")

    result = calculator_if(value1, value2, operation)
    print(f"Result: {result}")

    # Запит користувача на продовження обчислень
    continue_calculation = input("Do you want to continue calculating? (yes/no): ")
    if continue_calculation.lower() != "yes":
        break