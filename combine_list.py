
n = int(input("Enter the number of courses: "))
course_codes = []
course_names = []
print("Enter the course codes:")
for i in range(n):
    code = input(f"Course code {i+1}: ")
    course_codes.append(code)
print("Enter the course names:")
for i in range(n):
    name = input(f"Course name {i+1}: ")
    course_names.append(name)
combined_list = [f"{code}:{name}" for code, name in zip(course_codes, course_names)]
print("Combined list of courses:", combined_list)
