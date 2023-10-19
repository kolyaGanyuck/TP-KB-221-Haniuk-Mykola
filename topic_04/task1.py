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
      

def main():       
        value1 = genIntValue("Enter the first integer (x): ")

        value2 = genIntValue("Enter the second integer (y): ")
    
        operation = get_operation()
    
        print(calculator_if(value1, value2, operation))

while True:
    main()
    continue_calculation = input("Do you want to continue calculating? (yes/no): ")
    if continue_calculation.lower() != "yes":
        break



