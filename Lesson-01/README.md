# Lesson 1: Python Fundamentals - Operators, Data Types and variables
## Lesson overview
In this lesson  I learn about the basics of Python. The lesson covers variables, data types, operators, input/output, built-in functions and basic logic. 

## Learning objectives
- Ask for user input and use it in your program
- Use operators correctly
- Writing conditional statements
- Evaluate logical expressions and determine whether they are 'True' or 'False'
## What is Python used for?
- Web development (server-side)
- Datascience & Analytics
- Machine learning & AI

## Input  & Output
- Input: Data your program receives from the user
  - ``name = input("Enter your name: ")  # user types something``
  

- Output: Data your program send out
  - ``print("Hello, world!")  # output to console``

## Datatypes
- integer
- string
- float
- boolean
- None

## Pseudocode
Pseudocode is not a real programming code. It is used to think through logic and steps. It's a way to plan or describe a program or algorithm using plain, human-readable language instead of actual code.

## Variables
- Variables are used to store information, which we can use later in our program.
- The value of a variable can be used or modified at any time and can be of any data type.
- It is convention to write variable names in snake_case, and they cannot be reserved words like "return".

## Built-in functions
Built-in functions are always available without needing to import anything.

| Function  | Purpose                                                                            |
|-----------|------------------------------------------------------------------------------------|
| `len()`   | Returns the length of a sequence (string, list, tuple, etc.)                       |
| `type()`  | Returns the data type of a variable or value                                       |
| `int()`   | Converts a value to an integer (if possible)                                       |
| `float()` | Converts a value to a float (if possible)                                          |
| `str()`   | Converts a value to a string (if possible)                                         |
| `bool()`  | Converts a value to boolean (`True` or `False`, if possible)                       |
| `sum()`   | Returns the sum of all elements in a sequence                                      |
| `min()`   | Returns the smallest value in a sequence                                           |
| `round()` | Rounds a number to the nearest integer, or to a specified number of decimal places |
| `abs()`   | Returns the absolute value of a number (distance from zero)                        |



## Operators
### Arithmetic operators (NL: Rekenkundige operatoren)
| Operator | Name           | Example       |
|----------|----------------|---------------|
| `+`      | Addition       | `3 + 2 = 5`   |
| `-`      | Subtraction    | `5 - 2 = 3`   |
| `*`      | Multiplication | `4 * 2 = 8`   |
| `/`      | Division       | `5 / 2 = 2.5` |
| `%`      | Modulus        | `5 % 2 = 1`   |
| `**`     | Exponentiation | `2 ** 3 = 8`  |
| `//`     | Floor division | `5 // 2 = 2`  |

### Logical operators (NL: Logische operatoren)
| Operator | Name | Example                  |
|----------|------|--------------------------|
| `and`    | AND  | `True and False = False` |
| `or`     | OR   | `True or False = True`   |
| `not`    | NOT  | `not True = False`       |


### Comparison operators (NL: Vergelijkingsoperatoren)
| Operator | Name                  | Example         |
|----------|-----------------------|-----------------|
| `==`     | Equal to              | `5 == 5 = True` |
| `!=`     | Not equal to          | `5 != 3 = True` |
| `>`      | Greater than          | `5 > 3 = True`  |
| `<`      | Less than             | `3 < 5 = True`  |
| `>=`     | Greater than or equal | `5 >= 5 = True` |
| `<=`     | Less than or equal    | `3 <= 5 = True` |

### Assignments operators (NL: Toekenningsoperatoren)
| Operator | Name                    | Example                  |
|----------|-------------------------|--------------------------|
| `=`      | Assignment              | `x = 5`                  |
| `+=`     | Add and assign          | `x += 3` = `x = x + 3`   |
| `-=`     | Subtract and assign     | `x -= 2` = `x = x - 2`   |
| `*=`     | Multiply and assign     | `x *= 4` = `x = x * 4`   |
| `/=`     | Divide and assign       | `x /= 2` = `x = x / 2`   |
| `%=`     | Modulus and assign      | `x %= 3` = `x = x % 3`   |
| `**=`    | Exponent and assign     | `x **= 2` = `x = x ** 2` |
| `//=`    | Floor divide and assign | `x //= 2` = `x = x // 2` |

### Identity operators (NL: Identiteitsoperatoren)
| Operator | Name    | Example                                              |
|----------|---------|------------------------------------------------------|
| `is`     | IS      | `x is y = True if x and y are the same object`       |
| `is not` | IS NOT  | `x is not y = True if x and y are different objects` |

### Membership operators (NL: Lidmaatschapsoperatoren)
| Operator | Name      | Example                     |
|----------|-----------|-----------------------------|
| `in`     | IN        | `'a' in 'cat' = True`       |
| `not in` | NOT IN    | `5 not in [1, 2, 3] = True` |