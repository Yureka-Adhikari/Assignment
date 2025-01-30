import random
import string

def generate_password (length):
   if length< 6:
       return "Password Length Must Be At Least 6 Characters!"
   lowerCase_Char = string.ascii_lowercase
   upperCase_Char = string.ascii_uppercase
   digits = string.digits
   specialChar = string.punctuation
   password = [random. choice (lowerCase_Char), random. choice (upperCase_Char), random.choice(digits), random.choice(specialChar)]
   allCharTogether = lowerCase_Char + upperCase_Char+ digits + specialChar
   password = password + random.choices (allCharTogether, k = length - len(password))
   random.shuffle (password)
   
   return ' '.join(password)

password_length = random.randint(6,10)
password = generate_password (password_length)

print (f" Generated Password: {password}")