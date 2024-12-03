import numpy as np
shape = tuple(map(int, input("Enter the shape of the 3D arrays (e.g., 3 4 5): ").split()))
A1, A2 = np.random.randint(1, 101, size=shape), np.random.randint(1, 101, size=shape)

div_by_5 = A1[A1 % 5 == 0]
div_by_4 = A2[A2 % 4 == 0]
combined = np.concatenate((div_by_5, div_by_4))
size = int(np.sqrt(len(combined)))  
square_matrix = combined[:size**2].reshape(size, size)

print("Square Matrix:\n", square_matrix)
