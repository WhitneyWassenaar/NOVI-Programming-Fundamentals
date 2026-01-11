# Exercise: Write a function that calculates the average of a list of numbers.

# ---Personal practise---
# I redid the exercise multiple times to understand how dictionaries and functions work. I also think the original solution of the exercise did not match with what was asked.

# ---Grades---
grades = {"Java": 7, "Python": 8, "C#": 6, "HTML": 9, "CSS": 8}

def calculate_average (z):
    total = 0
    count = 0

    for x,y in z.items():
        total += y
        count += 1

    average = total/count
    return average

print(calculate_average(grades))

# ---Grades v1---
grades_v1 = {"Java": 7, "Python": 8, "C#": 6, "HTML": 9, "CSS": 8}

def calculate_average_v1 (z):
    total = 0
    count = 0

    for _,y in z.items(): # Use '_' for variables you don't use in the function. Convention, improves readability.
        total += y
        count += 1

    return total/count    # Removed variable 'average'. It's shorter and understandable

print(calculate_average_v1(grades_v1))

# ---Grades v2---
grades_v2 = {"Java": 7, "Python": 8, "C#": 6, "HTML": 9, "CSS": 8}

grades_v2 = list(grades_v2.values())

def calculate_average_v2(value_list):            # Use a list of values from the dictionary
    average = (sum(value_list)/len(value_list))
    return average

print(calculate_average_v2(grades_v2))

# ---Grades v3---
# Final solution
grades_v3 = {"Java": 7, "Python": 8, "C#": 6, "HTML": 9, "CSS": 8}

grades_v3 = list(grades_v3.values())

def calculate_average_v3(value_list):
    return sum(value_list)/len(value_list)

print(calculate_average_v3(grades_v3))

# ---Colors---
colors = {"red": 22, "blue": 2, "yellow": 4, "green": 9}

def calculate_average_1(z):
    return  sum(z.values())/len(z)

print(calculate_average_1(colors))

# ---Solution---
grades = {"Java": 7, "Python": 8, "C#": 6, "HTML": 9, "CSS": 8}
average = sum(grades.values()) / len(grades)

# ---My thoughts about the exercise---
# The exercise asks you to write a function. The original solution shows an expression. It does not show a function or a list.