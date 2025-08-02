'''l=input().split()
for s in l:
   if (all(ch in '01234567' for ch in s)):
       print(f"{s} contains only octal number")
   else:
       print(f"{s} dosent contain octal number") '''
'''import re
email = input("Enter email address: ")
match = re.match(r'([^@]+)@([^\.]+)\.(.+)', email)
if match:
    d = match.group(1)
    domain = match.group(2)
    ufix = match.group(3)
    print(f"User: {d}")
    print(f"Domain name: {domain}")
    print(f"Suffix: {ufix}")
else:
    print("Invalid email address")'''
'''import re
text = "a very very; irregular _sentences"
# Replace ';' and '_' with spaces, then normalize spaces
regular = re.sub(r'[;_]', ' ', text)
regular = re.sub(r'\s+', ' ', regular).strip()
print(regular)  # Output: a very very irregular sentences
 '''
        