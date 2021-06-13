# a tuple is a collection which is ordered and unchangeable
	# items have a defined order, and that order will not change
	# we cannot change, add or remove items after the tuple has been created 

# create a tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# can get around tuple modification limitations by converting it to a list and then back
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

# "unpack" a tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# if the number of variables is less than the number of values,
	# you can add an * to the variable name and the values will be assigned to the variable as a list
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits


