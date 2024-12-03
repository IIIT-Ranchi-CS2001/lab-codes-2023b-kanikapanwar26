def my_zip(customer_name, customer_id, shopping_points, strct=True):
    if strct:
        if len(customer_name) == len(customer_id) == len(shopping_points):
            return [(customer_name[i], customer_id[i], shopping_points[i]) for i in range(len(customer_name))]
        else:
            return "Lists are of unequal length"
    else:
        min_len = min(len(customer_name), len(customer_id), len(shopping_points))
        return [(customer_name[i], customer_id[i], shopping_points[i]) for i in range(min_len)]
customer_name = ['Ron', 'Harry', 'Harmione']
customer_id = [101, 102, 103]
shopping_points = [250, 150, 300]

print(my_zip(customer_name, customer_id, shopping_points, strct=True))  
print(my_zip(customer_name, customer_id, shopping_points[:2], strct=False))  