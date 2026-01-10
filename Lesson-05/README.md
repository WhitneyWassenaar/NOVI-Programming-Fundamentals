# Lesson 5: Dictionaries, Sets and Libraries

## Lesson Overview

In this lesson, we will explore three important Python concepts:

1. **Dictionaries** – Learn how to store and access data using key-value pairs.  
2. **Sets** – Understand unordered collections of unique elements and how to manipulate them.  
3. **Libraries** – Discover Python’s standard and external libraries, how to install and import them, and how to use them effectively in our projects.  
---

### Learning objectives
- Create, modify, and access **dictionaries** in Python.  
- Use **set methods** to add, remove, and manipulate elements.  
- Identify and utilize **Python standard libraries** for common tasks.  
- Install and import **external libraries** using `pip` and virtual environments (venv).  
- Understand and use **print parameters** (`sep` and `end`) to format output.  
- Apply **import statements** effectively, including aliases using `as`.  
- Compare Python **data structures** (lists, tuples, sets, dictionaries) in terms of order, mutability, and duplication.
---
**How to add a Python venv to IDE**
1. Settings
2. Project
3. Add interpreter
4. Local
5. New
6. Activate the venv in the terminal (windows) ```.\.venv\Scripts\activate```
---

### Standard Python Libraries

Python comes with many built-in libraries that do **not** need to be installed. Key categories include:

| Category                         | Examples / Libraries                     | Description                                 |
|----------------------------------|------------------------------------------|---------------------------------------------|
| File and Directory Management    | `os`, `shutil`, `pathlib`                | Work with files and folders                 |
| Networking                       | `socket`, `http.client`, `ftplib`        | Network communication                       |
| Web and Internet                 | `urllib`, `urllib.request`, `webbrowser` | Web requests and browsing                   |
| Cryptography and Security        | `hashlib`, `hmac`, `ssl`                 | Encryption, hashing, and secure connections |
| Multithreading & Multiprocessing | `threading`, `multiprocessing`, `queue`  | Parallel and concurrent execution           |
| Regular Expressions              | `re`                                     | Pattern matching in strings                 |


### Popular Python Libraries by Category

| Category           | Libraries               | Description                                     |
|--------------------|-------------------------|-------------------------------------------------|
| Computer Science   | `numpy`, `scipy`        | Numerical computing and scientific calculations |
| Data Analysis      | `pandas`                | Data manipulation and analysis                  |
| Data Visualization | `matplotlib`            | Creating charts and plots                       |
| Web Development    | `django`, `flask`       | Building web applications                       |
| Web Scraping       | `BeautifulSoup`         | Extracting data from websites                   |
| Machine Learning   | `tensorflow`, `pytorch` | Machine learning and deep learning frameworks   |

---
### Set Methods

| Method                            | Description                                                                     |
|-----------------------------------|---------------------------------------------------------------------------------|
| `add(element)`                    | Adds an element to the set.                                                     |
| `update(iterable)`                | Adds multiple elements from an iterable (list, set, tuple, etc.) to the set.    |
| `remove(element)`                 | Removes an element from the set. Raises `KeyError` if the element is not found. |
| `discard(element)`                | Removes an element if it exists; does nothing if the element is not found.      |
| `pop()`                           | Removes and returns a random element from the set. Raises `KeyError` if empty.  |
| `clear()`                         | Removes all elements from the set.                                              |
| `union(other_set)`                | Returns a new set with all elements from both sets.                             |
| `intersection(other_set)`         | Returns a new set with elements common to both sets.                            |
| `difference(other_set)`           | Returns a new set with elements in the first set but not in the second.         |
| `symmetric_difference(other_set)` | Returns a new set with elements in either set but not both.                     |
| `issubset(other_set)`             | Returns `True` if the set is a subset of another set.                           |
| `issuperset(other_set)`           | Returns `True` if the set is a superset of another set.                         |
| `copy()`                          | Returns a shallow copy of the set.                                              |

### Dictionary Methods

| Method         | Description                                                                 | Example                               |
|----------------|-----------------------------------------------------------------------------|---------------------------------------|
| `clear()`      | Removes all items from the dictionary                                       | `my_dict.clear()`                     |
| `copy()`       | Returns a **shallow copy** of the dictionary                                | `new_dict = my_dict.copy()`           |
| `fromkeys()`   | Creates a new dictionary from keys with a default value                     | `dict.fromkeys(['a','b'], 0)`         |
| `get()`        | Returns the value for a key, or `None` if the key does not exist            | `my_dict.get('name')`                 |
| `items()`      | Returns a view object of key-value pairs                                    | `my_dict.items()`                     |
| `keys()`       | Returns a view object of the dictionary's keys                              | `my_dict.keys()`                      |
| `values()`     | Returns a view object of the dictionary's values                            | `my_dict.values()`                    |
| `pop()`        | Removes the key and returns its value                                       | `my_dict.pop('age')`                  |
| `popitem()`    | Removes and returns the **last inserted** key-value pair                    | `my_dict.popitem()`                   |
| `setdefault()` | Returns the value of a key; if key doesn’t exist, inserts it with a default | `my_dict.setdefault('city', 'Paris')` |
| `update()`     | Updates dictionary with key-value pairs from another dictionary or iterable | `my_dict.update({'age':30})`          |

### Comparison of Python Data Structures

| Data Structure | Ordered?            | Mutable? | Allows Duplicates?    |
|----------------|---------------------|----------|-----------------------|
| List           | Yes                 | Yes      | Yes                   |
| Tuple          | Yes                 | No       | Yes                   |
| Dictionary     | Yes (version 3.7+ ) | Yes      | Keys: No, Values: Yes |
| Set            | No                  | Yes      | No                    |

---
### Print Parameters in Python

Python's `print()` function has two useful optional parameters: **`sep`** and **`end`**.

---

#### `sep` (separator)
The `sep` parameter defines what is placed **between multiple values** when printing.

**Example:**
```python
print("A", "B", "C", sep="-")
```
```python
"""A-B-C"""
```
---
### `end` Parameter in Python

The `end` parameter defines what is printed at the **end of the output**.

**Example:**
```python
print("Hello", end="!")
print("World")
```
```python
"Hello!World"
```
---
### `from ... import ... as ...` in Python

Python allows you to import specific parts of a library and optionally give them an alias using `as`.

**Syntax:**
```python
from module_name import function_or_class as alias_name
```