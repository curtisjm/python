# delcare a list 
fruits = ["apple", "banana", "cherry", "apple", "cherry"]
print(fruits)

# insert items at a specified index
fruits.insert(2, "watermelon")
# add items to the end
fruits.append("orange")

# can contain different data types
list1 = ["abc", 34, True, 40, "male"]

# append elements from one list to another
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)

# the extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)

# remove specified item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")

# remove specified index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
# can also do it with del keyword
del thislist[0]
# can also use it to delete the entire list
del thislist

# empty a list
thislist = ["apple", "banana", "cherry"]
thislist.clear()

# loop through a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
	print(x)
# use list comprehention short hand
[print(x) for x in thislist]
# can also use their index
for i in range(len(thislist)):
	print(thislist[i])

# list comprehention
# syntax: newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
# does the same thing as:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
# ex: only accepts numbers less than 5
newlist = [x for x in range(10) if x < 5]

# list objects have a sort() method that will sort the list alphanumerically, ascending, by default
# sort alphabetically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
# sort numberically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
# sort in descending order
thislist.sort(reverse = True)

# custom sort function with key = function
# sort based on how close the number is to 50
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)

# case-insensitive sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
# use str.tolower as key
thislist.sort(key = str.lower)

# reverse the current order of a list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()

# copy a list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()

# join lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
