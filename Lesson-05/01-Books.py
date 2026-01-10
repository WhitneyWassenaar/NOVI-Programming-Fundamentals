# You work at a library, and you have 2 lists with data about the rented books.
# Answer the questions with the help of sets and dictionaries

# === DATA ===
# Group 1

group_1 = ["Harry Potter", "The Hobbit", "The Da Vinci Code", "The Hobbit", "The Da Vinci Code", "Twilight", "The Fifth Wave", "Harry Potter", "The Hobbit"]
group_2 = ["The Da Vinci Code", "The Alchemist", "Harry Potter", "The Hobbit", "Twilight", "The Hunger Games", "Gone Girl", "Twilight", "The Hobbit"]



# === QUESTIONS ===
# 1.1 Create 2 sets from the books that are rented by group 1 and group 2

# My solution
# group_1_set = {"Harry Potter", "The Hobbit", "The Da Vinci Code", "The Hobbit", "The Da Vinci Code", "Twilight", "The Fifth Wave", "Harry Potter", "The Hobbit"}
# group_2_set = {"The Da Vinci Code", "The Alchemist", "Harry Potter", "The Hobbit", "Twilight", "The Hunger Games", "Gone Girl", "Twilight", "The Hobbit"}

group_1_set = set(group_1)
group_2_set = set(group_2)

# 1.2 Which books are unique to group 1 and group 2?
print(group_1_set^group_2_set)

# 2. Which books are rented by both groups?
print(group_1_set.intersection(group_2_set))

# 3.1 Which books are only rented by group 1 and not group 2?
print(group_1_set.difference(group_2_set))

# 3.2 Which books are only rented by group 2 and not group 1?
print(group_2_set.difference(group_1_set))

# 4.1 Create a dictionary for group 1 where the name of the books are the 'keys' and the amount of rental 'values'

# This is a list of tuples
# Each tuple contains a list and an empty dictionary
dictionaries = [(group_1, {}), (group_2, {})]

for group, dictionary in dictionaries: # The tuple contains: (group, dictionary)
    for book in group:                 # Go through every book in the group
        if book not in dictionary:     # If the book is not already in the dictionary
            dictionary[book] = 1       # Create a key [book] and add in the dictionary, then give the key [book] the value: 1
        else:                          # If the key [book] is already in the dictionary
            dictionary[book] += 1      # Add 1 to the value
print(dictionaries[0][1])
print(dictionaries[1][1])

# 5 Which book has been rented the most by group 1 and by group 2?

# count1 and count 2 are tuples (book, count).
count1 = ("", 0)
count2 = ("", 0)

# You want to count for each book how many times it has been rented.
# dictionaries is a list of tuples [(group_1,{}),(group_2,{})]

for book, count in dictionaries[0][1].items(): # items() returns the key value pair of the group_1 dictionary
    if count1[1] < count:                      # For each item in the dictionary the for loop checks if the count is lower dan the actual count1.
        count1 = (book, count)                 # if the item in the dictionary is higher than the count1, the count1 will update to this item.

for book, count in dictionaries[1][1].items():
    if count2[1] < count:
        count2 = (book, count)

print("Group 1 count: ", count1)
print("Group 2 count: ", count2)

