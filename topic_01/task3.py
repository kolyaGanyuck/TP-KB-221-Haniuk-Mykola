def discriminant(a, b, c):
    D = b**2 - 4*a*c
    return D

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

print(discriminant(a, b, c))