from math import *

print("Sides of scalene triangle:")
a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

Perimeter = a + b + c
print("Perimeter of scalene triangle is:", Perimeter)

s = Perimeter / 2
Area = sqrt(s * (s - a) * (s - b) * (s - c))
print("Area of scalene triangle is:", Area)

A = degrees(acos((b**2 + c**2 - a**2) / (2 * b * c)))
print("Angle between side b and c:", A)

B = degrees(acos((a**2 + c**2 - b**2) / (2 * a * c)))
print("Angle between side a and c:", B)

C = degrees(acos((a**2 + b**2 - c**2) / (2 * a * b)))
print("Angle between side a and b:", C)

