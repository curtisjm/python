# while loop
i = 1
while i < 6:
	print(i)

# for loop through a list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
	print(x)

# break statement used to exit the loop if a condition is met
fruits = ["apple", "banana", "cherry"]
for x in fruits:
	if x == "banana":
		break
	print(x)

# continue statement used to stop the current iteration of the loop and continue with the next
fruits = ["apple", "banana", "cherry"]
for x in fruits:
	if x == "banana":
		continue
	print(x)

# range function is used to loop through a set of code a specified number of times
for x in range(6):
	print(x)
# use a start parameter
for x in range(2, 6):
	print(x)
# increment by parameter
for x in range(2, 30, 3):
	print(x)
