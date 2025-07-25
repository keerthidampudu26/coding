#code to take a text data anf fetch to match the given data
"""syntax re.match(searchedelement,text)"""
import re 
t='hi students how are you!'
se=r'hi'
o=re.match(se,t)
if o:
    print("match found for :",o)
else:
    print("no match")