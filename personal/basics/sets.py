# a set is a collection which is both unordered and unindexed.
# sets are unchangeable, meaning that we cannot change the items after the set has been created.
# you can add new items

# create a set
thisset = {"apple", "banana", "cherry"}
print(thisset)

# you can't access items of a set with index, but you can loop through a set with the in keyword
for x in thisset:
	print(x)

# add and item
thisset.add("orange")

# add items from another set into the current se
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)


