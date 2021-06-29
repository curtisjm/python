# create a class
class MyClass:
	x = 5

# instantiate an object
p1 = MyClass()
print(p1.x)

# all classes have a function called __init__(), which is always executed when the class is being initiated
# use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created
# create a class named Person, use the __init__() function to assign values for name and age:
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# create a function in a class
	def myfunc(self):
		print("Hello my name is " + self.name)

p1 = Person("John", 36)
print(p1.name)
print(p1.age)
