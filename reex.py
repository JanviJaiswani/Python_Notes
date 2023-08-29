import re
pattern = r"apple"
pettern1 = r"\d+"
text = "I have 123 apple and 342 banana."

match1= re.findall(pettern1,text)
print(match1)

match = re.search(pattern, text)
if match:
    print("Pattern found:", match.group())
else:
    print("Pattern not found.")
