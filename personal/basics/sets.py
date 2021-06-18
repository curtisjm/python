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

# delete an item
# remove() will raise an error if item does not exist
thisset.remove("banana")
# discard() will not raise an error
thisset.discard("banana")

# join two sets
# new set with items from both given
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
# insert items from one set into another
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
# items that are present in both lists
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
# items that are not present in both lists
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)


