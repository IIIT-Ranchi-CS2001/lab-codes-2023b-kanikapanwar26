names=[name for name in input("Enter name:").split()]
roll_nos=[int(x) for x in input("Enter the roll numbers:").split()]
marks=[int(x) for x in input("Enter the  marks:").split()]
students=[]
for i in range(len(names)):
    students.append((names[i],roll_nos[i],marks[i]))
n = len(students)
for i in range(n):
    for j in range(0, n-i-1):
        if students[j][2] > students[j+1][2]:
            students[j], students[j+1] = students[j+1], students[j]  
for student in students:
    print(student)  

