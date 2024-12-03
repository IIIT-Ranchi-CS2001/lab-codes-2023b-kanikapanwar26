import numpy as np

shape = tuple(map(int, input("Enter the shape of the 3D arrays (e.g., 3 4 5): ").split()))
A1 = np.random.randint(1, 100, size=shape)
print("\nArray A1:\n", A1)
print("\nElements of A1 divisible by 5:\n", A1[A1 % 5 == 0])

