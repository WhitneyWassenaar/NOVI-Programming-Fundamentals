# Lesson 2: Control structures

## Lesson overview
In this lesson I learn about how to properly use different types of **control structures** in Python.

## Learning objectives
**Comments**
- Explain why something happens, not ***what** the code does
- The code should be self-explanatory; improve your code instead of adding comments that explains what it does

**Standard tags**

- `TODO` - Mark improvements or tasks to do
- `FIXME` - Mark problems or code that needs fixing
- You can acces these tags from the TODO menu in the IDE

**Control structures**


| Control Structure       | Description                                                                                                             |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------|
| `if / elif / else`      | Conditional statements. Execute code only if certain conditions are true.                                               |
| `for`                   | Loop over a sequence (list, string, range, etc.) a fixed number of times. <br/>(You know the amount of times it has to loop) |
| `while`                 | Loop as long as a condition remains true. <br/>(You don't know how many times it loops)                                      |
| `break`                 | Exit the current loop immediately.                                                                                      |
| `continue`              | Skip the rest of the current loop iteration and continue with the next.                                                 |



**Dungeon Game**
- Building a Dungeon Game with a minimum of 3 layers, 2 if-statements till the end
- Validate input
- Use draw.io to visualize idea

## Short Summary of What I Learned

- If you have elif in your if statement, and for example you have 3 elif's, only the first elif that evaluates to True will execute, and the rest will not be checked.


- i represents the current number in range.
  - So if you use range(1, 11), i will take the values 1 through 10 and will be printed each time.
  

- You can put a condition inside curly braces {} to check if it is True or False.

  - Example:
  ```python
    print(f'{john} is equal to {john} : {john == john}')
    ```


