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

## Regular Expressions for Text Processing

Regular expressions (regex) are powerful patterns used for searching, matching, and manipulating text. Python's `re` module provides comprehensive regex support for advanced text processing tasks.

### Importing the re Module

```python
import re
```

### Basic Pattern Matching

```python
# Search for a pattern
text = "The quick brown fox jumps over the lazy dog"
match = re.search(r"fox", text)
if match:
    print("Found:", match.group())  # Output: Found: fox

# Find all occurrences
emails = re.findall(r"\b\w+@\w+\.\w+\b", text_with_emails)
```

### Common Regex Patterns

- `.`: Any single character
- `^`: Start of string
- `$`: End of string
- `*`: Zero or more occurrences
- `+`: One or more occurrences
- `?`: Zero or one occurrence
- `{n}`: Exactly n occurrences
- `{n,}`: n or more occurrences
- `{n,m}`: Between n and m occurrences
- `[]`: Character class (e.g., `[a-z]`, `[0-9]`)
- `|`: Alternation (OR)
- `()`: Grouping
- `\d`: Digit (equivalent to `[0-9]`)
- `\w`: Word character (equivalent to `[a-zA-Z0-9_]`)
- `\s`: Whitespace character
- `\b`: Word boundary

### Common Regex Operations

#### Matching Patterns

```python
# Match at the beginning
if re.match(r"^Hello", text):
    print("Text starts with Hello")

# Full string match
if re.fullmatch(r"\d{3}-\d{2}-\d{4}", ssn):
    print("Valid SSN format")
```

#### Searching and Finding

```python
# Find first occurrence
match = re.search(r"\d+", text)  # Find first number

# Find all occurrences with positions
matches = re.finditer(r"\b\w{5,}\b", text)  # Words with 5+ characters
for match in matches:
    print(f"Word: {match.group()}, Position: {match.start()}-{match.end()}")
```

#### Substitution

```python
# Replace patterns
cleaned = re.sub(r"\s+", " ", text)  # Replace multiple spaces with single space
censored = re.sub(r"\b\d{4}\b", "****", text)  # Censor 4-digit numbers
```

#### Splitting

```python
# Split on regex pattern
parts = re.split(r"[,\s]+", text)  # Split on commas or spaces
```

### Compiling Regex Patterns

For better performance when using the same pattern multiple times:

```python
pattern = re.compile(r"\b\d{3}-\d{3}-\d{4}\b")  # Phone number pattern
matches = pattern.findall(text)
```

### Flags

Modify regex behavior with flags:

```python
# Case-insensitive matching
re.search(r"hello", text, re.IGNORECASE)

# Multiline mode
re.search(r"^start", multiline_text, re.MULTILINE)

# Dot matches newlines
re.search(r"begin.*end", text, re.DOTALL)
```

### Practical Examples

#### Email Validation
```python
def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None
```

#### Extracting URLs
```python
urls = re.findall(r"https?://[^\s]+", text)
```

#### Phone Number Formatting
```python
def format_phone(number):
    # Remove non-digits
    digits = re.sub(r"\D", "", number)
    # Format as (XXX) XXX-XXXX
    return re.sub(r"(\d{3})(\d{3})(\d{4})", r"(\1) \2-\3", digits)
```

### Best Practices for Regex

1. **Use raw strings** (`r"pattern"`) to avoid backslash escaping issues
2. **Compile patterns** for repeated use to improve performance
3. **Be specific** with your patterns to avoid unintended matches
4. **Test thoroughly** with various inputs
5. **Consider alternatives** like string methods for simple operations
6. **Use comments** in complex patterns with `re.VERBOSE` flag
7. **Handle exceptions** - regex operations can raise exceptions

### Common Pitfalls

- Forgetting word boundaries (`\b`) when matching whole words
- Not accounting for case sensitivity
- Overusing `.*` which can be greedy
- Not escaping special characters when matching literals

## Further Reading

- [Python String Documentation](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
- [String Methods Reference](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Python re Module Documentation](https://docs.python.org/3/library/re.html)
- [Regex101](https://regex101.com/) - Online regex tester and debugger 

