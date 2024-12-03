def my_max(*container):
    if not container:
        return None  
    max_value = container[0]
    for value in container:
        if value > max_value:
            max_value = value

    return max_value
list_data = [3, 5, 1, 8, 2]
print("Max in list:", my_max(*list_data))
set_data = {7, 2, 9, 4}
print("Max in set:", my_max(*set_data))
tuple_data = (1, 3, 7, 4, 2)
print("Max in tuple:", my_max(*tuple_data))
