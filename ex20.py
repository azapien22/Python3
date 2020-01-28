# ex20: Functions and Files

# Import arg variables from the system library 
from sys import argv

# Assign the first and the second arguments to the two variables
script, input_file = argv

# Define a function called print_all to print the whole contents of a file
# with one file object as formal parameter. "f" is just a variable name for the file. 
def print_all(f):
    print(f.read())

# Create a function to go to the beginning of a file
# (i.e.. byte 0)
def rewind(f):
    f.seek(0)

# Create a function to print out one line. Where
# line_count is the line number we want to read,
# f is the name of the file(from above), and
# Readline is a built-in function or method.
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

# Will display whole file in the console
print("First let's print the whole file:\n")

# Will display whole file in the console
print_all(current_file)

print("Now lets rewind, kind of like a tape.")

# Call the rewind function to go back to the beginning of the file
rewind(current_file)

print("Lets print three lines:")
# Now the process of incrementing begins
# Set current line to 1
current_line = 1
print_a_line(current_line, current_file) 

# Set current line to 2 by adding 1
current_line +=  1
print_a_line(current_line, current_file)

# Set current line to 3 by adding 1
current_line += 1
print_a_line(current_line, current_file)