import hashlib
filename= input("Enter the filename: ")
try:
   with open(filename,"rb") as file:
      data = file.read()

   hash_value = hashlib.sha256(data).hexdigest()
 #object gets created,hash is computed,immediately converted to a hexadecimal string
   expected_hash = input("Enter expected hash: ").strip()
   if hash_value == expected_hash:
    print("Hash matched. File is unchanged.")
   else:
    print("Hash did not match. File may have been modified.")
except FileNotFoundError:
  print("file not found")