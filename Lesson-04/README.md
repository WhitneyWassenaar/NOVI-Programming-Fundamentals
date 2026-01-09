# Lesson 4: Control Structures and Lists

## Lesson Overview
In this lesson, we explore Python's compound data types, focusing on lists and tuples, as well as control structures such as loops. We will learn how to store multiple values in a single variable, manipulate them, and iterate over them efficiently.


## Learning Objectives
- Understand the difference between lists and tuples
- Create and manipulate lists and tuples
- Access elements using indexes and slicing
- Use list methods to add, remove, or modify elements
- Write for loops and while loops to iterate over collections
- Store multiple values in a single compound data type

### Tuple
A tuple is an immutable collection of elements. Tuples are defined using parentheses () with elements separated by commas. Unlike lists, once a tuple is created, its elements cannot be changed.
```python
tuple = (1, 2, 3, 4)
```

### List
A list is a mutable collection of elements. Lists allow modification, addition, and removal of elements. Python provides built-in methods to work with lists efficiently.

```python
list = [1, 2, 3, 4, 5]
```
**Indexing**
```python
print(list[0])
```

**Slicing**
```python
print(my_list[1:4])
```

## List Methods

| Method    | Description                                | Example               |
|-----------|--------------------------------------------|-----------------------|
| `append()` | Adds an element to the **end** of the list | `list.append(10)`     |
| `insert()` | Adds an element at a **specific position** | `list.insert(1, 20)`  |
| `remove()` | Removes an element by **value**            | `list.remove(10)`     |
| `pop()`    | Removes an element by **index**            | `list.pop(0)`         |
