# === LIST COMPREHENSION ===
# Use a list comprehension to create a list of even numbers between 1 and 20

numbers = [x for x in range(1,20) if x % 2 == 0]
print(numbers)

# === CREATING A LIST ===
# Determine and print the sum of all elements in the list `numbers` using a for-loop.

# === VERSION 1 ===
numbers = [2, 5, 7, 11, 15]
print(sum(numbers))

# === VERSION 2 ===
numbers = [2, 5, 7, 11, 15]
total = 0
for i in numbers:
    total += i
print(total)


# === LIST FUNCTIONALITIES ===
# Create the list table_of_three = [3, 6, 9, 12, 16, 18, 24, 27, 32]. You can see that some values are incorrect.

# Use assignment to change 16 to 15
# Use the remove() method to delete 32
# Use the append() method to add 30 to the end of the list
# Use the insert() method to add 21 between 18 and 24
# Print the list. Is the table now correct?

table_of_three = [3, 6, 9, 12, 16, 18, 24, 27, 32]

table_of_three[4] = 15
table_of_three.remove(32)
table_of_three.insert(6, 21)
table_of_three.append(30)

print(table_of_three)


# Take the list names = ['Alfred', 'Bob', 'Charlie', 'David', 'Erik']

# Print the first 3 names
# Replace David and Erik with ['Daphne', 'Eva', 'Frederique'] and print the result

# === SLICES ===
names = ['Alfred', 'Bob', 'Charlie', 'David', 'Erik']
print(names)
names[3:5] = 'Daphne', 'Eva', 'Frederique'
print(names)


# === LIST COMPREHENSION ===
# Use list comprehension to create a list of all even numbers between 1 and 20.

even_numbers = [i for i in range(1, 21) if i % 2 == 0]
print(even_numbers)


# ================================

# === OTHER NOTES ON LISTS AND TUPLES ===

# Print the middle items of a list
shopping_list = ['Milk', 'Butter', 'Cheese', 'Eggs', 'Meat']
print(shopping_list[1:4])

# Print specific items from a list
grades = [7.7, 8.3, 5.3, 6.7]
print(f'First item in grades list: {grades[0]}')
print(f'Last item in grades list: {grades[-1]}')
print(f'Last item in grades list (hard way): {grades[len(grades)-1]}')
# len() gives 5, but index goes up to 4. So subtract 1 to get the last item. Otherwise, you get "list index out of range".

# Remove an item from a list
animals = ['cow', 'horse', 'pig', 'chicken']

removed_animal = animals.pop()  # pop() stores the value in a variable
print(f'From the animals list: {animals}, {removed_animal} has been removed.')

# Use del
del animals[0]  # Removes item
print(animals)

# Use remove()
# remove() only deletes the first occurrence if duplicates exist
numbers = [1, 4, 2, 6, 7, 8, 54, 3, 2]
numbers.remove(2)
print(numbers)

# Use a for loop to remove all '3's
# A copy is made because in a for loop, indexes shift when items are removed. Using a copy avoids this.
# The for loop iterates over the copy, but modifies the original list to remove all '3's.

# === CORRECT WAY ===
numbers_list = [1, 3, 6, 8, 4, 5, 66, 22, 6, 3]
copy_list = list(numbers_list)

for i in copy_list:
    if i == 3:
        numbers_list.remove(3)

print(numbers_list)

# === INCORRECT WAY ===
numbers_list = [1, 3, 6, 8, 4, 5, 66, 22, 6, 3]
copy_list = list(numbers_list)

for i in copy_list:
    if i == 3:
        copy_list.remove(3)

print(numbers_list)

# A list is iterable
letter_list = ['H', 'a', 'l', 'l', 'o']
print("".join(letter_list))

# Print a list in reverse
letter_list.reverse()
print(letter_list)  # prints as a list

print("".join(letter_list))  # prints as a string

# Double the values in a list
number_list = [1, 3, 5, 8, 9]
for number in number_list:
    print(f'The value doubled: {number * 2}')

tuple_list = [(1, 4), (2, 6), (6, 7)]
for x, y in tuple_list:
    print(f'The product of {x} and {y} is: {x * y}')

# coordinate is the item in the list
# coordinate item is a tuple, you can access index 0 and 1
coordinate_list = [(2, 5), (7, 8), (3, 5)]
for coordinate in coordinate_list:
    print(f'{coordinate[0]},{coordinate[1]}')

# Shorter way
for x, y in coordinate_list:
    print(f'Coordinate ({x},{y})')

# Print a list in uppercase using a for loop
# 1. Loop over the word list
# 2. Convert each word to uppercase
# 3. Append the uppercase word to the uppercase list
words = ['book', 'computer', 'pen', 'pencil', 'calculator']
uppercase_list = []

for word in words:
    uppercase_word = word.upper()
    uppercase_list.append(uppercase_word)
print(uppercase_list)

# enumerate converts each item in the list into a tuple with a number: (0,item), (1,item), etc.

# === VERSION 1 ===
for index, word in enumerate(words):
    print(f'The {index}th word is {word}')

# === VERSION 2 ===
# enumerate counts from 0, which may not read logically. You can set the starting number yourself (optional).
# The first word is still 'book'
for index, word in enumerate(words):
    print(f'The {index}th word is {word}')
