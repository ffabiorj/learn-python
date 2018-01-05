import re

randStr = "F.B.I I.R.S CIA F.F.F.F."

# match words with dots
print("Mathes", len(re.findall(".\..", randStr)))

long_string = """A very very very very very very
long line in a ver very very very 
long variable
"""

regex = re.compile(" ")

replace_newline = regex.sub("-", long_string)
print(replace_newline)