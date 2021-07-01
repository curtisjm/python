# create a parent class
class Person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname

	def printname(self):
		print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

# to create a class that inherits the functionality from another class,
	# send the parent class as a parameter when creating the child class
class Student(Person):
	pass
# use the Student class to create an object,
	# and then execute the printname method:
x = Student("Mike", "Olsen")
x.printname()

# the child's __init__() function overrides the inheritance of the parent's __init__() function:
class Student(Person):
	def __init__(self, fname, lname):
		x = 1
    	# add properties etc

# to keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
class Student(Person):
	def __init__(self, fname, lname):
		Person.__init__(self, fname, lname)

# super() function will make the child class inherit all the methods and properties from its parent:
class Student(Person):
	def __init__(self, fname, lname):
		super().__init__(fname, lname)
		# add a property called graduationyear to the Student class:
		self.graduationyear = 2019

# add a year parameter, and pass the correct year when creating objects:
class Student(Person):
	def __init__(self, fname, lname, year):
		super().__init__(fname, lname)
		self.graduationyear = year
x = Student("Mike", "Olsen", 2019)

# add a method called welcome to the Student class:
class Student(Person):
	def __init__(self, fname, lname, year):
		super().__init__(fname, lname)
		self.graduationyear = year

	def welcome(self):
		print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# if you add a method in the child class with the same name as a function in the parent class,
	# the inheritance of the parent method will be overridden.