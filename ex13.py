# Ex.13 Parameters, Unpacking, Variables
'''In this exercise we will cover one more input method you can use to pass variables to a script'''

from sys import argv
# Read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)

print("Your first variable is:", first)

print("Your second variable is:", second)

print("Your third variable is:", third)