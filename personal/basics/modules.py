# consider a module to be the same as a code library, a file containing a set of functions you want to include in your application.

# create a module:
	# save this code in a file named mymodule.py
def greeting(name):
	print("Hello, " + name)

person1 = {
	"name": "John",
	"age": 36,
	"country": "Norway"
}

# use a module:
	# import the module named mymodule, and call the greeting function:
import mymodule

mymodule.greeting("Jonathan")

# access variables from within a module
a = mymodule.person1["age"]
print(a)

# you can create an alias when you import a module, by using the as keyword:
import mymodule as mx

a = mx.person1["age"]
print(a)

# there is a built-in function to list all the function names (or variable names) in a module. The dir() function:
	# list all the defined names belonging to the platform module:
import platform

x = dir(platform)
print(x)

# you can choose to import only parts from a module, by using the from keyword.
from mymodule import person1

print (person1["age"])