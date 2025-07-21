import os
f="cmduser.py"
if os.path.exists(f):
	size=os.path.getsize(f)
	print(f"{f}  size:{size} bytes.")
else:
	print("file not found")