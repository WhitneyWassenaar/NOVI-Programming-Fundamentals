# EdHub  
# Programming Fundamentals Exercises Chapters 5 and 6

This repository contains a collection of exercises from EdHub and lesson preparation.

---

## Contents
These exercises focus on practicing `if/else` statements.

### Calculator :heavy_plus_sign::heavy_minus_sign:
You will create a simple calculator that takes 2 numbers as input and an operator (`+`, `-`, `/`, `*`). You will ensure that the correct calculation is performed based on the operator.

### Pizza_Plaza :pizza:
You work at a pizzeria, but they don’t have a convenient system to calculate the price of a pizza. You, as a programmer, are hired to solve this. You need to consider the size of the pizza and extra toppings.

### Treasure :lock:
You arrive on an island where you can make choices. Each choice leads to a different location. It’s possible that you can’t continue playing after, for example, falling into a hole.

### Password :closed_lock_with_key:
Write a program that asks the user for a password. The user has a maximum of 3 attempts to enter the correct password. If the correct password is entered, print a success message and exit the loop. If the user enters the wrong password 3 times, display a message saying access is denied.

### Random Number :1234:
In this exercise, you will write a script where the user must guess a secret number.

### Change (Cash) :money_with_wings:
Write a program for cashiers where you input an amount (in cents), for example, 87 cents, and the program returns how many coins of 50, 20, 10, 5, and 1 cent should be given back.

---

## Short Summary of What I Learned

### Calculator :heavy_plus_sign::heavy_minus_sign:
- Exception handling is unnecessary for string inputs. For `int` or `float` inputs, there is a higher chance of a `ValueError`, so exception handling is useful.  
- Using a while loop ensures the user can retry input if the previous input was invalid.

---

### Pizza_Plaza :pizza:
- The biggest challenge was writing code as short and efficient as possible. I often started too big and detailed, making the code more error-prone.  
- I aimed to create a short but efficient version, reaching version six. Making it shorter made it illogical.  
- Example: You shouldn’t be able to order pepperoni or cheese without a pizza. I enforced this in the code.  
- Important logic tip: When checking multiple conditions in a print statement, use `and` instead of `or`:
```python
if size != 'S' and size != 'M' and size != 'L':
    print('Apparently you didn’t want to order a pizza')
```
- Lists can be created directly in the condition:
```python
if size in ['S', 'M', 'L']:
    print(f'Pizza {size}, total €{total}')
else:
    print('You did not choose a pizza')
```
---
# Treasure :lock:
For the first time, I understand what ASCII art is. For this assignment, I used an image-to-ASCII converter website [https://www.asciiart.eu/image-to-ascii](https://www.asciiart.eu/image-to-ascii) to quickly create ASCII art. I chose Code page 437 as the ASCII gradient.  

I added an input after the last print statement in case you run the code in Python.  
If the program ends, you wouldn’t see the last print statement, so I added an extra input:  
```python
input("Press enter to quit the game")
```

# Password 🔐

I noticed I spent too much time on the condition of the `while` loop. Often, there was a bug in the code where an error appeared if the answer was entered correctly on the third attempt. I made it unnecessarily difficult for myself. Should I start the `while` loop with a fixed number of attempts or run it as long as the correct password hasn't been entered?

There was also a case where a variable was underlined in yellow, which means it wasn’t defined. Should we avoid that, or is it okay occasionally?

In this exercise, it was important to understand which factor has the highest priority. What weighs more: the number of attempts to enter a password, or when the correct password is entered? The order matters a lot.

# Random number 🔢

In Python, `random.randInt(1,10)` and `random.randomInt(1,10)` do **NOT** work!  
`random.randint(1,10)` **does** work.  
Both `1` and `10` are included in `random.randint(1,10)`.

# Change 💰

If we use a variable multiple times in `if` statements, its value can change (or be overwritten) depending on which condition is executed.

I now know how to use a tuple in combination with functions.  
The parameter of a function can have almost any name, and when calling the function, you can pass an existing variable as an argument.

# Project Information 📄
This is partly an EdHub assignment and lesson preparation from the Programming Fundamentals track of the Web Development bootcamp at NOVI University of Applied Sciences.
