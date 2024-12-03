def grade(marks):
    if marks >= 90:
        return 10, "OUTSTANDING"
    elif marks >= 80:
        return 9, "VERY GOOD"
    elif marks >= 70:
        return 8, "GOOD"
    elif marks >= 60:
        return 7, "AVERAGE"
    elif marks >= 50:
        return 6, "PASS"
    else:
        return 0, "FAIL"


name = input("Enter the student's name: ")
roll_number = input("Enter the student's roll number: ")
marks = float(input("Enter the marks secured in Mathematics out of 100: "))


grade_point, remark = grade(marks)


print("\nStudent Details:")
print(f"Name: {name}")
print(f"Roll Number: {roll_number}")
print(f"Marks: {marks}")
print(f"Grade Point: {grade_point}")
print(f"Remark: {remark}")

