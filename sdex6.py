# Exercise 6. Strings and Text

types_of_people = 10

x = f"There are {types_of_people} types_of_people"

binary = "binary"

do_not = "don't"

y = f"Those who know {binary} and those who {do_not}"

print(x)

print(y)

print(f"I said: {x}")

print(f"I also said: '{y}'")

hilarious = False

joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation)

# .format fills in the empty variable in joke_evaluation
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."

e = "a string with a right side."

# Adding a + sign concatenates w & e
print(w + e)

# .format fills in the variable
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

# .format fills in the empty variable
txt = "For only {} dollars!"
print(txt.format(60))