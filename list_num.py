import statistics
numbers=[int(x) for x in input("Enter the numbers:").split()]
mean=statistics.mean(numbers)
mode=statistics.mode(numbers)
median=statistics.median(numbers)
print(f"Mean is {mean}")
print(f"Mode is {mode}")
print(f"Median is {median}")