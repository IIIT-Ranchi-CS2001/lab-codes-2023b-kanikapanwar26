students = {input("Enter name: "): int(input("Enter marks: ")) for _ in range(5)}
high_performers = []
average_performers = []
low_performers = []
for name, marks in students.items():
    if marks >= 85:
        high_performers.append(name)
    elif 60 <= marks < 85:
        average_performers.append(name)
    else:
        low_performers.append(name)
print(f"High Performers ({len(high_performers)}):", high_performers)
print(f"Average Performers ({len(average_performers)}):", average_performers)
print(f"Low Performers ({len(low_performers)}):", low_performers)
top_student = max(students, key=students.get)
print(f"Top Performer: {top_student} with {students[top_student]}%")

