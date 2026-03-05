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
- [Regex101](https://regex101.com/) - Online regex tester and debugger 

