names=[name for name in input("Enter name:").split()]
roll_nos=[int(x) for x in input("Enter the roll numbers:").split()]
marks=[int(x) for x in input("Enter the  marks:").split()]
students=list(zip(names,roll_nos,marks))
print(students)
sorted_students=sorted(students,key=lambda x:x[2])
for students in sorted_students:
  print(students)