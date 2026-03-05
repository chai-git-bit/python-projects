import re

text = "Red moon and red sun are in the sky. The red color is beautiful."
pattern = r"red"

findall = re.findall(pattern, text)
if findall:
    print("Pattern found:", findall)
else:
    print("Pattern not found")
