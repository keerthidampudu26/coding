import re
octal_pattern = re.compile(r'^[0-7]+$')
strings = ['789', '123', '004']
for s in strings:
    if octal_pattern.match(s):
        print(f"'{s}' is a valid octal number.")
    else:
        print(f"'{s}' is NOT a valid octal number.")
