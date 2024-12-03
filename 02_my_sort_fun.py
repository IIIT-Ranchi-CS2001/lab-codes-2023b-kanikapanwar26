def my_zip(customer_name, customer_id, shopping_points, strct=True):
    if strct and not (len(customer_name) == len(customer_id) == len(shopping_points)):
        return "Lists are of unequal length"
    min_len = min(len(customer_name), len(customer_id), len(shopping_points))
    return [(customer_name[i], customer_id[i], shopping_points[i]) for i in range(min_len)]

def my_sort(data, key):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][key] > data[j+1][key]:
                data[j], data[j+1] = data[j+1], data[j]
    return data
customer_name = ['Alice', 'Bob', 'Charlie']
customer_id = [101, 102, 103]
shopping_points = [250, 150, 300]

data = my_zip(customer_name, customer_id, shopping_points, strct=True)
if isinstance(data, list):
    print("Sorted by name:", my_sort(data, key=0))
    print("Sorted by customer ID:", my_sort(data, key=1))
    print("Sorted by shopping points:", my_sort(data, key=2))
else:
    print(data)

