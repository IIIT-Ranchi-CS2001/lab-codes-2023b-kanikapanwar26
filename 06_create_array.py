import numpy as np

def Create_Array(*args):
    size = len(args)
    array = np.zeros((size, size), dtype=int)
    np.fill_diagonal(array, args)
    
    return array
result = Create_Array(1, 2, 3, 4)
print(result)
