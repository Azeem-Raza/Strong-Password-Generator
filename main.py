""" Password Generator """
import random
import string#For accessing string constants

total = string.ascii_letters + string.digits + string.punctuation
#ASCII- is a system that is used to represent characters digitally
#Digits- All the digits in the Arabic numeral system
#Punctuation-special characters
while True:

    try:
        length = int(input("Enter the length of Password: "))
        if length < 8:
            print("Your number should be at least 8.")
            length = input("Please, Enter your number again: ")
        else:
            break
    except:
        print("Please, Enter numbers only.")
        length = input("How many characters do you want in your password? ")

password = "".join(random.sample(total, length))

print(password)
