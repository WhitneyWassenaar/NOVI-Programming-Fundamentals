# Lesson 6: Functions

## Lesson Overview



## Learning Objectives

## Short summary what I've learned

### Using a seperator in a list
Seperator is an **argument / parameter** in a print statement
- If you want to separate a list with a character, you can't use sep=" " and only the list in the print statement, because this is just 1 argument to separate and that's not possible. The list will be printed as is

```python
my_list = ["one", "two", "three"]
print(my_list, sep=" and ")
# Output: ['one', 'two', 'three']
```

- You have to unpack the list to target the list items by using *. This way, the list wil be separated in multiple arguments.
```python
my_list = ["one", "two", "three"]
print(*my_list, sep=" and ")
# Output: one and two and three
```

- Or you can use the **method**: join()
```python
my_list = ["one", "two", "three"]
print(" and ".join(my_list))
# Output: one and two and three
```

### What if you want to use different seperators in a list?
What if you want to use the seperators: "and", "," at the same time in a list?  

Example: ```my_list = ["one", "two", "three"]``` changes to  ```"one, two and three"```

```python
my_list = ["one", "two", "three"]
print(", ".join(my_list[:2]) + " and " + my_list[-1])
# Output: one, two and three
```
