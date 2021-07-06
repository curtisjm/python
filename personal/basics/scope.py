# if you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
def myfunc():
	global x
	x = 300
	
myfunc()
print(x)

# also, use the global keyword if you want to make a change to a global variable inside a function.
x = 300

def myfunc():
	global x
	x = 200

myfunc()
print(x)

