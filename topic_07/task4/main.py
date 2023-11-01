from calculator import *
def main():
    calculator = Calculator()

    while True:
        value1 = calculator.gen_int_value("Enter the first integer (x): ")
        value2 = calculator.gen_int_value("Enter the second integer (y): ")
        operation = calculator.get_operation()
        result = calculator.perform_operation(value1, value2, operation)
        print(result)

        continue_calculation = input("Do you want to continue calculating? (yes/no): ")
        if continue_calculation.lower() != "yes":
            break

if __name__ == "__main__":
    main()