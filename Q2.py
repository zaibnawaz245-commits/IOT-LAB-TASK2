name = input("Enter student's name: ")
roll_no = input("Enter roll number: ")

marks = []
for i in range(1, 6):
    m = float(input(f"Enter marks for subject {i}: "))
    marks.append(m)

total = sum(marks)
percentage = (total / 500) * 100

if percentage >= 80:
    grade = "A+"
elif percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

if min(marks) < 40:
    result = "Fail"
    grade = "F"
else:
    result = "Pass"

print("\n--- Student Marksheet ---")
print("Name:", name)
print("Roll No:", roll_no)
for i, m in enumerate(marks, 1):
    print(f"Subject {i}: {m}")
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Result:", result)