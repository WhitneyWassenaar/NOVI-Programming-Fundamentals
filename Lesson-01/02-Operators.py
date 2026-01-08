# ==========================================
# Example exercise
# Write the notation for 10 million. Use Python's "readability method"
# print the number
# ==========================================
print(10_000_000)  # The result is: 10000000

# ==========================================
# Exercise 1:
# Which number is correctly written according to the "readability method"?
# print the number.

#     100_00.000_001
#     1_000.00_001
#     1_000_000.000_1
# ==========================================
print(1_000_000.000_1)

# ==========================================
# Exercise 2:
# How do you write the following numbers in Python's scientific notation?
# print the numbers.

#     -12.000.000
#     0.13 with three extra zeros (0.00013)
#     64.000.000.000
# ==========================================
print(-12e6)
print(0.13e-3)
print(64e9)

# ==========================================
# Exercise 3:
# Write 5 million. How do you turn that into 0.05 from using scientific notation?
# ==========================================
# 5.000.000
print(5000000e-8)

# == CORRECT NOTATION ===
# I forgot to apply the "readability method"
print(5_000_000)
print(5_000_000e-8)
# ==========================================
# Exercise 4:
# What is the right answer? Try to think in advance whether the answer will be an integer or a float. Check your answer by printing it.

# a. 11 * 3
# b. 7.5 – 1.5
# c. 3 + 4.0
# d. 15 / 5
# ==========================================
# a. int   (Because 11 and 3 are whole numbers, and multiplying them will still give a whole number)
# b. float (Because when you calculate with a float, the result will also be a float)
# c. float (Because when you calculate with a float, the result will also be a float)
# d. float (Because when you divide numbers, the result will always be a float)

# ==========================================
# Exercise 5:
# What is the right answer? Try to think in advance whether the answer will be an integer or a float. Check your answer by printing it.
# a. 18 // 4
# b. 15.5 // 4
# c. 10 % 4
# d. 9 % 4.5
# ==========================================
# a. int (Because with floor division the result remains an int if you use int numbers, don’t confuse it with /!)
# b. float (Because with floor division the result becomes a float, the result is rounded down, but remains a float since 15.5 is a float.)
# c. int (Because the result is 2, it's an int.)
# d. float (Because one of the numbers is a float, the result is also a float)

# ==========================================
# Exercise 6:
# Below are a number of expressions. Write for yourself in a comment what the order of operations is and calculate the answer. Then check with a print statement if you get the same result.

#  A 8 + 2 * 3
#  B (8 + 2) * 3
#  C 2 ** 3 ** 2
#  D (2 ** 3) ** 2
#  E 100 - 5 ** 2 / 5 * 2
# ==========================================
# A 2 * 3 = 6 , 8 + 6 = 14                              | * has higher precedence than +
# B (8 + 2) = 10, 10 * 3 = 30                           | () comes before everything, then *
# C 3 ** 2 = 9, 2 ** 9 = 512                            | If you only have exponentiation in the calculation, you work from right to left.
# D (2 ** 3) = 8, 8 ** 2 = 64                           | () comes before everything, then *
# E 5 ** 2 = 25, 25 / 5 = 5, 5 * 2 = 10, 100 -10 = 90.0   | First **, then /, then *, and lastly subtraction

print(8 + 2 * 3)
print((8 + 2) * 3)
print(2 ** 3 ** 2)
print((2 ** 3) ** 2)
print(100 - 5 ** 2 / 5 * 2) # In the solution, it says the result is 85, but that’s not correct; it should be 90.0

# ==========================================
# Exercise 7:
# Convert the following text into a Python string. Pay attention to special characters and spaces
# Tip: You can print repeating words multiple times using an operator
# Check the result with a print statement

# A: This is the shape of a roof / \
# B: ‘quotes’ ‘quotes’ ‘quotes’ ‘quotes’ spamspamspam
# C: Python’s syntax is “simple”
# ==========================================

print('This is the shape of a roof / \\')
print("'quotes'" * 4, "spam" * 3) # In the solution, it says 3 * 'quotes', but I clearly read 'quotes' four times.
print(""" Python's  syntax is "simple" """)

# === ALTERNATIVE WAY ===
print("Python's  syntax is \"simple\"")