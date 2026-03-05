# Strings in Python

## Overview of Data Types in Python

In programming, a data type is a classification that specifies which type of value a variable can hold. Python supports several built-in data types, including:

- **Numeric Types**: `int`, `float`, `complex`
- **Sequence Types**: `str` (strings), `list`, `tuple`
- **Mapping Type**: `dict`
- **Set Types**: `set`, `frozenset`
- **Boolean Type**: `bool`
- **Binary Types**: `bytes`, `bytearray`
- **None Type**: `NoneType`

This README focuses specifically on strings (`str`), one of the most commonly used data types in Python.

## What are Strings in Python?

Strings in Python are sequences of characters enclosed in single quotes (`'`), double quotes (`"`), or triple quotes (`'''` or `"""`). They are immutable, meaning once created, their contents cannot be changed.

### Creating Strings

```python
# Single quotes
name = 'Alice'

# Double quotes
greeting = "Hello, World!"

# Triple quotes for multi-line strings
multiline = """This is a
multi-line string"""
```

### String Immutability

Strings are immutable, so operations that appear to modify a string actually create a new string:

```python
s = "hello"
s = s.upper()  # Creates a new string "HELLO"
```

## Common String Operations

### Concatenation
Joining strings together:

```python
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2  # "Hello World"
```

### Length
Get the number of characters:

```python
text = "Python"
length = len(text)  # 6
```

### Indexing and Slicing
Access individual characters or substrings:

```python
s = "Python"
first_char = s[0]      # 'P'
last_char = s[-1]      # 'n'
substring = s[1:4]     # 'yth'
```

### Case Conversion

```python
text = "Hello World"
upper = text.upper()   # "HELLO WORLD"
lower = text.lower()   # "hello world"
title = text.title()   # "Hello World"
```

### Searching and Replacing

```python
text = "Hello World"
position = text.find("World")  # 6
replaced = text.replace("World", "Python")  # "Hello Python"
```

### Splitting and Joining

```python
text = "apple,banana,cherry"
fruits = text.split(",")  # ['apple', 'banana', 'cherry']
joined = "-".join(fruits)  # "apple-banana-cherry"
```

### Stripping Whitespace

```python
text = "  Hello World  "
stripped = text.strip()  # "Hello World"
```

## String Methods

Python provides numerous built-in string methods:

- `capitalize()`: Capitalizes the first character
- `count(substring)`: Counts occurrences of substring
- `endswith(suffix)`: Checks if string ends with suffix
- `startswith(prefix)`: Checks if string starts with prefix
- `format()`: Formats string with placeholders
- `isalnum()`, `isalpha()`, `isdigit()`, `islower()`, `isupper()`: Character checks
- `lstrip()`, `rstrip()`: Strip from left/right
- `partition(sep)`: Splits into three parts
- `zfill(width)`: Pads with zeros

## String Formatting

### f-Strings (Python 3.6+)
```python
name = "Alice"
age = 30
message = f"My name is {name} and I am {age} years old."
```

### format() Method
```python
message = "My name is {} and I am {} years old.".format(name, age)
```

### % Operator (older style)
```python
message = "My name is %s and I am %d years old." % (name, age)
```

## Escape Sequences

- `\\n`: Newline
- `\\t`: Tab
- `\\\\`: Backslash
- `\\'` or `\\"` : Quote characters

Use raw strings (`r"..."`) to avoid escaping backslashes.

## Examples in This Directory

This directory contains example Python scripts demonstrating various string operations:

- `string-concat.py`: String concatenation
- `string-len.py`: Getting string length
- `string-lowercase.py`: Converting to lowercase
- `string-replace.py`: Replacing substrings
- `string-split.py`: Splitting strings
- `string-strip.py`: Removing whitespace
- `string-substring.py`: Extracting substrings

Each file contains a simple example with comments explaining the operation.

## Best Practices

1. Use f-strings for string formatting when possible (Python 3.6+)
2. Remember strings are immutable - operations create new strings
3. Use appropriate quote types to avoid excessive escaping
4. Consider string methods for common operations rather than manual implementation
5. Use `join()` for concatenating multiple strings efficiently

## Further Reading

- [Python String Documentation](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
- [String Methods Reference](https://docs.python.org/3/library/stdtypes.html#string-methods) 

