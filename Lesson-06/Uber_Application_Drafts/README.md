# About Uber Application Drafts
This directory contains drafts from the Uber application exercise. It was an exercise that required a lot of patience and understanding. Through this exercise, I learned how to build a clear structure for an application.

You know that feeling when you worked on your code hours or days ago, and now you no longer understand what you wrote or what your code does, and you feel like starting over? That feeling comes from not fully understanding the fundamentals of your code. When I experienced this, I decided to start over multiple times, and teach myself the basics — in my case, functions, comments, docstrings, dictionaries, properties etc.

## Functions
**Basic**
- Choose from 3 different uber services
- User can enter distance
- The application calculates the total price of a ride

**Bonus**
- User can view history of booked rides
- User can choose a preferred service
- Before booking a ride, the user will be asked to choose from preferred service if chosen beforehand or choose for a different service

## Pseudocode
My pseudocode is a bit too abstract. It is a great way to write down a structure of my thought proces, but it could not easily be converted to real code.
```python

"""
**---Basic---**

libraries
- menu-option: uber-service
- uber-service: price


menu
User chooses 1 service
- option 1
- option 2
- option 3

km
user enters distance
- input km

calculate total price
uber-service price * km

user can see total price
print statement

**---Bonus---**

start()

- [1] Change service ✔
- [2] View history ✔
- [3] Book a ride 

preference() 
- Select service ✔
- Update USER dict ✔
- back to start() ✔

history()
- check if history dict contains item ✔
- If not, go back to start ✔
- If yes, print history dict and go back to start() ✔

book_a_ride()
- Ask if user would like to select preferred service or select a different service ✔
- If user selects preferred service, check if USER dict has a preference ✔
- If yes, program selects USER["preference"] as choice ✔
- If not, go back to book_a_ride()

- If user selects a different service
- Ask distance

total_price()
- After km, calculate total price in total_price() 
- go back to start()


preference()
- {USER["preference]}

history()
- {USER["history]}

book_a_ride()
requires:
- ride_option value of preference() > shows user if preferred service is select with print statement
- ride_option value from own input > different_service()

different_service()
requires:
- preferred_service, if it exists
- Own input which service
- km

returns result from these values ((preferred_service of eigen invoer) ,km)

total_price()
requires:
input: preferred_service, if it exists or own input 
returns result input * km to calculate total price
"""
```
## Summary of what I've learned
- ``def different_service(preferred_service=None):`` This function has an optional parameter. It is not mandatory for preferred_service to have a value. It could also be ```None```
- Variables in capital are constants. Variables which the value never change
- Make a separate commit for each bug fix to improve traceability during code review.
- Write pseudocode that can easily be converted into real code.


## How does return work?

Example:
1. In function_1(), we ask the user for input.
2. We want to use variable_1 in function_2(), so we pass it as a parameter
3. To enter variable_1 in function_2() as a parameter, inside function_1(), write function_2(variable_1)
4. function_2() returns 2 values: result_multiply and variable_2
5. Add these variables before function_2(variable_1) `` result_multiply, variable_2 = function_2(variable_1)``
6. Now, function_1() picks up the values of function_2()
7. The purpose of return in function_1() is if you want to use these variable outside this function.  
That is ```return result_multiply, variable_2```
``` python
def function_1():
    variable_1 = int(input())                             
    result_multiply, variable_2 = function_2(variable_1)
    
    return result_multiply, variable_2

def function_2(param):
    result_multiply = param * 2
    variable_2 = input()

    return result_multiply, variable_2
```

## Input Validation with Try/Except
**BUG**: Whenever the user must select an option, if the input was not entered as a valid value, the error message ``"Only numbers are allowed, try again"`` was printed in the terminal. However, this approach is confusing, because if an input requires a string, the same message would still appear, which does not make sense.

**Problem**: The issue is that the ``try/except`` block is wrapped around all options, including calls to other functions that may require different types of input.

**Solution**: Place the ``try/except`` block only around the input itself. This way, only the input is checked, rather than all the functions.

```python
def start():
    while True:
        try:
            start_option = int(input("---Start---\n"
                                     "[1] Change service preference\n"
                                     "[2] View history\n"
                                     "[3] Book a ride\n"
                                     "\n"
                                     "Enter a number: "))
            if start_option == 1:
                preference()
                continue


            elif start_option == 2:
                history()
                continue


            elif start_option == 3:
                service_option, km = book_a_ride()
                total_price(service_option, km)

            else:
                print("Invalid number, try again\n")
                continue
        except ValueError:
            print("Only numbers are allowed, try again\n")

start()
```