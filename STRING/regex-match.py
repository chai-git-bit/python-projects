import re

text = "Kangaroos are marsupials that are native to Australia. They are known for their powerful hind legs and ability to hop."
pattern = r"Kangaroos"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")
