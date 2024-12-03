import math
import matplotlib.pyplot as plt

def process_numbers(numbers):
    primes, composites = [], []
    for num in numbers:
        if num < 2: continue
        for i in range(2, num):
            if num % i == 0: 
                composites.append(num)
                break
        else:
            primes.append(num)
    return [p**2 for p in primes], [math.sqrt(c) for c in composites]

numbers = [12, 7, 25, 3, 9, 17, 4, 5, 8, 19]
squares, square_roots = process_numbers(numbers)


fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].scatter([7, 3, 17, 5, 19], squares, color='blue')
axes[0].set_title("Prime Numbers vs Their Squares")
axes[1].scatter([12, 25, 9, 4, 8], square_roots, color='red')
axes[1].set_title("Composite Numbers vs Their Square Roots")
plt.tight_layout()
plt.show()
