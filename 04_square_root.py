import math

def separate_prime_and_composite(numbers):
    primes = []
    composites = []
    for num in numbers:
        if num < 2: continue
        for i in range(2, num):
            if num % i == 0: 
                composites.append(num)
                break
        else:
            primes.append(num)
    return primes, composites

def process_numbers(numbers):
    primes, composites = separate_prime_and_composite(numbers)
    return [p**2 for p in primes], [math.sqrt(c) for c in composites]
numbers = [12, 7, 25, 3, 9, 17, 4, 5, 8, 19]
squares, square_roots = process_numbers(numbers)
print("Square of primes:", squares)
print("Square root of composites:", square_roots)

