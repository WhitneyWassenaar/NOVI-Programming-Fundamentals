# ==========================================
# Example exercise:
# Declare two tuples named 'tuple_one' and 'tuple_two'.
# tuple_one gets the values 1, 2, and 3.
# tuple_two gets the values 4, 5, and 6.
# Make sure you end up with a tuple containing the values 1, 2, 3, 4, 5, and 6.
# Remember that tuples are immutable.
# ==========================================

tuple_one = (1, 2, 3)
tuple_two = (4, 5, 6)

# You must declare a new tuple variable.
# Existing tuples cannot be modified (unlike lists, which can use append, insert, or remove).
combined_tuple = tuple_one + tuple_two
print('combined tuple:', combined_tuple)  # Result: (1, 2, 3, 4, 5, 6)


# ==========================================
# Exercise 1:
# Create a tuple with the values 'b', 'c', 'a'.
# Print the values of the tuple in alphabetical order (a, b, c).
# Tip: Use the indices of the tuple.
#
# Expected output: a b c
# ==========================================
letters = ('b', 'c', 'a')
print(letters[2], letters[0], letters[1])


# ==========================================
# Exercise 2:
# Create the list 'number_square_pair' for the numbers 1 through 5,
# where each element consists of a tuple containing the number and its square.
# Use a list comprehension.
#
# Expected output: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
# ==========================================
number_square_pair = [(i, i**2) for i in range(1, 6)]
print(number_square_pair)


# ==========================================
# Exercise 3:
# Create a tuple named 'tuple_count' with the values 1, 2, 3, 4, 5.
# Reverse the order of the numbers.
# Make sure you create a new tuple with the values 5, 4, 3, 2, 1.
# Tip: Use the reversed() function.
#
# Expected output: (5, 4, 3, 2, 1)
# ==========================================

# === VERSION 1 ===
# A tuple cannot be modified directly, so you must use the tuple() function.
# This version is incorrect and will cause an error.

# tuple_count = (1, 2, 3, 4, 5)
# tuple_count_reversed = tuple_count(reversed(tuple_count))
# print(tuple_count_reversed)

# === VERSION 2 ===
# Correct solution using tuple()
tuple_count = (1, 2, 3, 4, 5)
tuple_count_reversed = tuple(reversed(tuple_count))
print(tuple_count_reversed)
