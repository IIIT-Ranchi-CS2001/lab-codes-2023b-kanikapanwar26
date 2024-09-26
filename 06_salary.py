employees = {}
for _ in range(5):
    name = input("Enter employee name: ")
    salary = float(input(f"Enter salary for {name}: "))
    employees[name] = salary
employee_list = list(employees.items())
n = len(employee_list)
for i in range(n):
    for j in range(0, n-i-1):
        if employee_list[j][1] < employee_list[j+1][1]:  
            employee_list[j], employee_list[j+1] = employee_list[j+1], employee_list[j]
print("\nSorted Employee Salaries:")
for rank, (name, salary) in enumerate(employee_list, start=1):
    print(f"{rank}. {name}: Rs. {salary:.2f}")
