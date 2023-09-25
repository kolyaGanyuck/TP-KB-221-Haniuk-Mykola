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

def calculator_match(value1, value2, operation):
     match operation:
        case '+': return add(value1, value2)
         
        case '-': return subtract(value1, value2)
         
        case '*': return multiply(value1, value2)
         
        case '/': return divide(value1, value2)
         
        case _: return "Error: Invalid operation"

# Input values and operation from the user
value1 = float(input("Enter the first value: "))
value2 = float(input("Enter the second value: "))
operation = input("Enter the operation (+, -, *, /): ")

result = calculator_match(value1, value2, operation)
print(f"Result: {result}")