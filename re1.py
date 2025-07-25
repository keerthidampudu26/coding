import re
octal_pattern = re.compile(r'^[0-7]+$')
string=['764','453','004']
result = octal_pattern.match(string)
if result:
    print("passed")
else:
    print("not passed")