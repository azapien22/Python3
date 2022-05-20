from sys import argv
from os.path import exists

script, from_file, to_file = argv

# print(f"Copying from {from_file} to {to_file}") REMOVED

# We could do these two on one line, how?
#in_file = open(from_file)
#indata = in_file.read()
in_file = open(from_file).read()


print(f"The input file is {len(in_file)} bytes long")

# print(f"Does the output file exist? {exists(to_file)}") REMOVED

# print("Ready, hit RETURN to continue, CTRL - C to abort.") REMOVED

# input() Removed, not neccessary

out_file = open(to_file, "w")
out_file.write(in_file)

# print("Alright, all done.") commented out as not neccesary

out_file.close()