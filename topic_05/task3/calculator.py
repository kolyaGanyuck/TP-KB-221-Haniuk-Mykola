from operations import calculator_if

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