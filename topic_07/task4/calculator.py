from functions import add, subtract, multiply, divide
import os
class Calculator:
    def __init__(self):
        self.log_file_name = "calculator_log.txt"
        self.script_directory = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(self.script_directory, self.log_file_name)

    def log_action(self, log_data):
        with open(self.file_path, 'a') as log_file:
            log_file.write(log_data)

    def perform_operation(self, value1, value2, operation):
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
        self.log_action(log_data)

        return result

    def gen_int_value(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                log_data = f"Entered: {value}\n"
                self.log_action(log_data)
                return value
            except ValueError:
                print("Value is not an integer")

    def get_operation(self):
        while True:
            try:
                operation = input("Enter the operation (+, -, *, /): ")
                if operation in ('+', '-', '*', '/'):
                    log_data = f"Selected operation: {operation}\n"
                    self.log_action(log_data)
                    return operation
                else:
                    raise ValueError("Invalid operation")
            except (ValueError, ZeroDivisionError) as e:
                print(f"Mistake: {e}")