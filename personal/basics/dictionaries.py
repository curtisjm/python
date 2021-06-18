# dictionaries are used to store data values in key:value pairs.
# a dictionary is a collection which is ordered (as of version 3.7), changeable and does not allow duplicates.

# create a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# print a value using its key
print(thisdict["brand"])

# get a list of keys in a dictionary
x = thisdict.keys()
# get a list of values
x = thisdict.values()

# add an item to the dictionary
thisdict["color"] = "white"

# get a list of each item as tuples
x = thisdict.items()

# print key names
for x in thisdict:
	print(x)
# print values
for x in thisdict:
	print(thisdict[x])
# print keys and values
for x, y in thisdict.items():
	print(x, y)

# copy a dictionary
mydict = thisdict.copy()

# create nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
