import os
from functions import add, subtract, multiply, divide
def calculator_if(value1, value2, operation):
    if operation == '+':
        result = add(value1, value2)
        action = "+"
    elif operation == '-':
        result = subtract(value1, value2)
        action = "-"
    elif operation == '*':
        result = multiply(value1, value2)
        action = "*"
    elif operation == '/':
        result = divide(value1, value2)
        action = "/"
    else:
        raise ValueError("Invalid operation")
    
    log_data = f"(Full info) Action: {action}, Data: {value1} {action} {value2}, Result: {result}\n"
    log_action(log_data)

    return result
        
def log_action(log_data):
    log_file_name = "calculator_log.txt"
    current_directory = os.path.dirname(os.path.abspath(__file__))
    log_file_path = os.path.join(current_directory, log_file_name)

    with open(log_file_path, 'a') as log_file:
        log_file.write(log_data)

def genIntValue(prompt: str):
    while True:
        try:
            value = int(input(prompt))
            log_data = f"Entered: {value}\n"
            log_action(log_data)
            return value
        except ValueError:
            print("Value is not an integer")

def get_operation():
    while True:
        try:
            operation = input("Enter the operation (+, -, *, /): ")
            if operation in ('+', '-', '*', '/'):
                log_data = f"Selected operation: {operation}\n"
                log_action(log_data)
                return operation
            else:
                raise ValueError("Invalid operation")
        except (ValueError, ZeroDivisionError) as e:
            print(f"Mistake: {e}")