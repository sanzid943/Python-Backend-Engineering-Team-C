# Student Result & Scholarship Checker

student_name = input("Enter student name: ")

english = float(input("Enter marks for English: "))
math = float(input("Enter marks for Math: "))
python = float(input("Enter marks for Python: "))

attendance = float(input("Enter attendance percentage: "))
income = float(input("Enter family monthly income: "))

# Calculate total and average
total = english + math + python
average = total / 3

print("\n--- Student Result ---")
print("Student Name:", student_name)
print("Total Marks:", total)
print("Average:", round(average, 2))

# Grade
if average >= 80:
    grade = "A+"
elif average >= 70:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "F"

print("Grade:", grade)

# Pass or Fail
if average >= 50 and english >= 40 and math >= 40 and python >= 40:
    print("Status: Pass")
else:
    print("Status: Fail")

# Scholarship eligibility
if average >= 80 and attendance >= 90 and income <= 30000:
    print("Scholarship: Eligible")
else:
    print("Scholarship: Not Eligible")