import os 
'''folder="cmdadd.py"
if not os.path.exists(folder):
	os.mkdir(folder)
	print(f"Folder '{folder}' created.......")
else:
	print(f"Folder '{folder}' already exists......")'''
path='.'
f=os.listdir(path)
print("files and folders in current directory")
for f1 in f:
	print(f1)
 