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


