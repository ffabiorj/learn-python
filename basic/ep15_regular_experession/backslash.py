import re 

string = "Here is \\stuff"

print("\\stuff: ", re.search(r"\\", string))
