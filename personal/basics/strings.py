# length of a string
a = "Hello, World!"
print(len(a))

# if a string contains something
txt = "The best things in life are free!"
if "free" in txt:
	print("Yes, 'free' is present.")
# check if it's not in the string 
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("Yes, 'expensive' is NOT present.")

# slicing strings
b = "Hello, World!"
# characters from 2 to 5
print(b[2:5])
# from start to 5
print(b[:5])
# from 2 to end
print(b[2:])

# splitting strings
a = "Hello, World!"
# returns ['Hello', ' World!']
print(a.split(",")) 

# format() takes arguments and places them where the placeholders {} are
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
# can have multiple placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
# can use indexes to specify where items go
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))