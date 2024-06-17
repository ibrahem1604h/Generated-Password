import random
import string
length = int(input("Enter the length of the password: "))
leters=int(input("Enter the number of leters: "))
numbers=int(input("Enter the number of numbers: "))
symbols=int(input("Enter the number of symbols: "))
total= leters+numbers+symbols
if total==length:
   char= random.choices(string.ascii_letters, k=leters)
   num= random.choices(string.digits, k=numbers)
   sym= random.choices(string.punctuation, k=symbols)
   password= char+num+sym
   random.shuffle(password)
   pssword=("").join(password)
   print(f"Generated Password: {pssword}")
else:
  print("Enter the correct number of characters")
