# List of students and their grades.
# Using a list of tuples
# Each tuple contains a student and their grade
# Create a list of tuples

# === VERSION 1 ===
# number_of_students = len(students) doesn't need to be inside the for loop
# else statement is not needed, if the condition is not true nothing happens.

students = [("Maria", 8.3), ("Arnold", 3.9), ("Alice", 5.7), ("Sven", 6.2)]
sum_grades = 0
best_student = ""
highest_grade = 0
number_of_students = 0

for student, grade in students:
    number_of_students = len(students)
    sum_grades += grade
    if grade > highest_grade:
        highest_grade = grade
        best_student = student
    else:
        highest_grade = highest_grade

    print(f'{student} - {grade}')


print(f'Average grade: {(sum_grades/number_of_students):.1f}')
print(f'The best student is {best_student} with a {highest_grade}')

# === VERSION 2 ===
# I moved number_of_students = len(students) out of the for loop and removed the else statement

students = [("Maria", 8.3), ("Arnold", 3.9), ("Alice", 5.7), ("Sven", 6.2)]
sum_grades = 0
best_student = ""
highest_grade = 0
number_of_students = len(students)

for student, grade in students:
    sum_grades += grade
    if grade > highest_grade:
        highest_grade = grade
        best_student = student

    print(f'{student} - {grade}')

print(f'Average grade: {(sum_grades/number_of_students):.1f}')
print(f'The best student is {best_student} with a {highest_grade}')
