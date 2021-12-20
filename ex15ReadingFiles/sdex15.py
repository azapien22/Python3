# Ex. 15 Reading Files

# It means “from the module sys, import the function or parameter argv”.
# The sys module contains all kinds of system-related functions and constants.
# The argv parameter returns the specific way the script was called (e.g. from a command line interface).
from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your {filename}:")

print(txt.read())

print("Type the filename again:")

file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())