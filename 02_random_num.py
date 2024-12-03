import random
K = int(input("Enter the number of random numbers (K): "))
N = int(input("Enter the upper limit (N): "))
if K < 10:
    print("The minimum value for K is 10. Setting K to 10.")
    K = 10
random_numbers = [random.randint(0, N) for _ in range(K)]
print(f"List of {K} random numbers within the range 0 to {N}:")
print(random_numbers)
