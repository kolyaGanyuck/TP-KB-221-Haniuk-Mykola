import math

def calculate_discriminant_and_roots(a, b, c):
    # formula
    discriminant = b ** 2 - 4 * a * c
    
    if discriminant > 0:
        # Two distinct roots
        sqrt_discriminant = math.sqrt(discriminant)

        root1 = (-b + sqrt_discriminant) / (2 * a)
        root2 = (-b - sqrt_discriminant) / (2 * a)

        return f"Two distinct real roots: root1 = {root1}, root2 = {root2}"
    
    elif discriminant == 0:
        # One root 
        root = -b / (2 * a)
        return f"One real root: root = {root}"
    
    else:
        # No roots
        return "No real roots "

# Input coefficients a, b, and c from the user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

result = calculate_discriminant_and_roots(a, b, c)
print(result)