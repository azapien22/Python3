# Study drill ex.11
'''Collecting user input in python using the input() functions'''
#Write another "form" to ask some more questions
email = input("Enter your email address:")
print("To confirm, is your email address:", email, "?")
option = input("Yes or No?")
print(option,"!", "Good!")
#Write another "form" to ask some more questions
user_age = input("Enter your Age:")
final_userAge = int(user_age) +1
print("On your next birthday, you'll be:", final_userAge)