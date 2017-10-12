types_of_people = 10									#sets types_of_people to 10

x = f"There are {types_of_people} types of people."		# takes the value of variable types_of_people and inserts in string

binary = "binary"										# sets binary to string "binary"
do_not = "don't"										# sets do_not to string "don't"
y = f"Those who know {binary} and those who {do_not}."	# Stríng input: binary and do_not

print(x)												# prints x
print(y)												# prints y

print(f"I said: {x}")									# string input x
print(f"I also said: '{y}'")							# string input y

hilarious = False										# sets bolean statement to false, also just sets hilarious to string false
joke_evaluation = "Isen't that joke so funny?! {}"		# joke_evaluation is set to question, {} allows us to "isnert" something with format

print(joke_evaluation.format(hilarious))
w = "This is a left side of ...."
e = "a string with a right side"

print(w + e)											# prints out first w and then e
														# w holds <text> and e holds text, adding them together will print out both w and e, in the order inserted into print.