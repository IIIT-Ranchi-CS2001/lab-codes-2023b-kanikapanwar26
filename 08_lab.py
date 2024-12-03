import math
def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        R1 = (-b + math.sqrt(discriminant)) / (2 * a)
        R2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"The equation has two distinct real roots: R1 = {R1}, R2 = {R2}")
    elif discriminant == 0:
        R1 = R2 = -b / (2 * a)
        print(f"The equation has one real repeated root: R1 = R2 = {R1}")
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        print(f"The equation has two complex roots: R1 = {real_part} + {imaginary_part}i, R2 = {real_part} - {imaginary_part}i")
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))
find_roots(a, b, c)
     