def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        return "Error: Division by zero"
    return result

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
    try:
       
        value1 = float(input("Enter the first value: "))
        value2 = float(input("Enter the second value: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue

    while True:
        operation = input("Enter the operation (+, -, *, /): ")
        if operation in ('+', '-', '*', '/'):
            break
        else:
            print("Invalid operation. Please enter +, -, *, or /.")

    result = calculator_if(value1, value2, operation)
    print(f"Result: {result}")

    continue_calculation = input("Do you want to continue calculating? (yes/no): ")
    if continue_calculation.lower() != "yes":
        break