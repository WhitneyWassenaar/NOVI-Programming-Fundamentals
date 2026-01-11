# Write a function that calculates the average of a list of numbers.

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


# ---Personal practise---

colors = {"red": 22, "blue": 2, "yellow": 4, "green": 9}

def calculate_average_1(z):

    return  sum(z.values())/len(z)

print(calculate_average_1(colors))

