parrot = "Norwegian Blue"
print(parrot)

# prints character at index
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

# prints character at index from end of the sting / in the negative direction
print(parrot[-1])
print(parrot[-14])

# slices string, last character not included. [start value : stop value
print(parrot[0:6])  # Norwreg. up to, but not including character 6.
print(parrot[3:5])

print(parrot[0:9])
print(parrot[:9])   # don't have to provide start value if starting form 0

print(parrot[10:14])
print(parrot[10:])  # start at value, goes until the end

print(parrot[:6] + parrot[6:])

# slice values can be negative
print(parrot[-4:2])

