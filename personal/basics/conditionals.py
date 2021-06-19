# if, elif, else
a = 200
b = 33
if b > a:
	print("b is greater than a")
elif a == b:
	print("a and b are equal")
else:
	print("a is greater than b")

# one line if
if a > b: print("a is greater than b")

# short had if else
print("A") if a > b else print("B")

# and keyword
a = 200
b = 33
c = 500
if a > b and c > a:
	print("Both conditions are True")

# or keyword
if a > b or a > c:
	print("At least one of the conditions is True")
