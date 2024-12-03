def separate_prime_and_composite(numbers):
    """Separate numbers into prime and composite lists."""
    primes = []
    composites = []
    
    for num in numbers:
        if num < 2: 
            continue
        for i in range(2, num):
            if num % i == 0:
                composites.append(num)
                break
        else:
            primes.append(num)
    
    return primes, composites
import random
K = 10
N = 50
random_numbers = [random.randint(0, N) for _ in range(K)]
print(f"Original List: {random_numbers}")


primes, composites = separate_prime_and_composite(random_numbers)
print(f"Prime Numbers: {primes}")
print(f"Composite Numbers: {composites}")

