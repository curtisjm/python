# declare a function
def my_function():
	print("Hello from a function")

# call a function
my_function()

# arbitrary arguments
# if you do not know how many arguments that will be passed into your function,
	# add a * before the parameter name in the function definition
# this way the function will receive a tuple of arguments
def my_function(*kids):
	print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

# keyword arguments with key = value syntax
def my_function(child3, child2, child1):
	print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# arbitrary keyword arguments
# if you do not know how many keyword arguments that will be passed into your function,
	# add two asterisk: ** before the parameter name in the function definition.
# this way the function will receive a dictionary of arguments
def my_function(**kid):
	print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

# default parameter value
def my_function(country = "Norway"):
	print("I am from " + country)
my_function("Sweden")
my_function()

# return values
def my_function(x):
	return 5 * x
print(my_function(5))
