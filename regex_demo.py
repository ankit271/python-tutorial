import re

s = '\section'
pattern = r'\\section'
result = re.findall(pattern, s)

print(result)
