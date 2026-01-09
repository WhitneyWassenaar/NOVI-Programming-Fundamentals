# === BONUS ===
# Ask the user to add students and grades to the list via 'input'
# Let the user search by name to see a specific student's grade
# Sort the list by grades and print them

students = []

while True:
    student_name = input('Student name: (Press x to finish input) ')
    if student_name == 'x':
        break
    grade_input = float(input('Grade: '))
    student_item = (student_name, grade_input)

    students.append(student_item)

# === SORT THE LIST BY GRADES ===
# sorted() returns a new list.
# By default, it sorts by the first element of each tuple. In this case, that would be the student's name.

# key=lambda x: x[1]
# key determines what to sort by.
# lambda x: x[1] means: for each item x (here a tuple (student_name, grade_input)), use the second element x[1]
# x = student_item
# x[0] = "student_name"
# x[1] = grade_input

# reverse=True
# By default, sorted() sorts from smallest to largest. Here we want the highest grade first, so we use reverse=True.

# sorted() creates a new list and does not change the original unless you assign it. For example: students = sorted(students)

students = sorted(students, key=lambda x: x[1], reverse=True)

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

search_name = input('Enter the name of a student to see their grade: ')
for student, grade in students:
    if search_name == student:
        print(f'{student}, {grade}')
