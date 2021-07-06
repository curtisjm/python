# an iterator is an object that contains a countable number of values.
# an iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

# lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
# all these objects have a iter() method which is used to get an iterator:
	# return an iterator from a tuple, and print each value:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

# strings are also iterable objects, containing a sequence of characters:
mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# we can also use a for loop to iterate through an iterable object:
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
	print(x)

# to create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
	# the __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
	# the __next__() method also allows you to do operations, and must return the next item in the sequence.
# create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):
class MyNumbers:
	def __iter__(self):
		self.a = 1
		return self

	def __next__(self):
		x = self.a
		self.a += 1
		return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# To prevent the iteration to go on forever, we can use the StopIteration statement.
	# previous example would go on forever
class MyNumbers:
	def __iter__(self):
   		self.a = 1
   		return self

	def __next__(self):
		if self.a <= 20:
			x = self.a
			self.a += 1
			return x
		else:
			raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
	print(x)