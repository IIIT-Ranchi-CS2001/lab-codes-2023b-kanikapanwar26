import numpy as np
shape = tuple(map(int, input("Enter the shape of the 3D arrays (e.g., 3 4 5): ").split()))
A1 = np.random.randint(1, 101, size=shape)
A2 = np.random.randint(1, 101, size=shape)
result = A2[A2 % 4 == 0]

print("A1:\n", A1)
print("A2:\n", A2)
print("Elements of A2 divisible by 4:\n", result)
