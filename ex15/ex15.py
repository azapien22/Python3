# ex15 : reading files

# Import argv variables from sys submodule
from sys import argv

# get the argv variables
script, filename = argv # pylint: disable=unbalanced-tuple-unpacking

# open a file
txt = open(filename)

# Print file name
print("Here's your file %r: " % filename)

# print all the contents of the file
print(txt.read())

# close the file
txt.close()

# prompt to type the file name again
print("Type the filename again:")

# input the new file name
file_again = input(">")

# open the new selected file
txt_again = open(file_again)

# print the contents of the new selected file
print(txt_again.read())

# close the file
txt_again.close()