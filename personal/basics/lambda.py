# a lambda function is a small anonymous function.
# a lambda function can take any number of arguments, but can only have one expression.
# syntax -- lambda arguments : expression

# declare and call
x = lambda a : a + 10
print(x(5))

# multiple arguments
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# use them as an anonymous function inside of another one
def myfunc(n):
	return lambda a : a * n

# use that function definition to make a function that always doubles the number you send in
def myfunc(n):
	return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))
