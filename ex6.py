# 10 types of people
types_of_people = 10
# x variable format string types of people variable end string
x = f"There are {types_of_people} types of people."
#binary variable
binary = "binary"
# Don't variable
do_not = "don't"
# y variable is set to format string and combines both binary and dont variables
y = f"Those who know {binary} and those who {do_not}."
#prints
print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}")
# hilarious variable set to false
hilarious = False
#joke evaluation  
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)