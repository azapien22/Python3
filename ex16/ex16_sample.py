# a script similar to ex16 that uses read and argv to read the file

from sys import argv

script, filename = argv

print("the contents of the file %s:" % filename)
target = open(filename)
contents = target.read()
print(contents)
target.close()