a = 12
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)    # float division
print(a // b)   # integer division, rounded down towards minus infinity
print(a % b)    # modulus, remainder after integer division

print()

for i in range(1, a // b):  # has to use integer division because other value is an int, python is strongly typed
    print(i)

# long had version of that for loop
i = 1
print(i)
i = 2
print(i)
i = 3
print(i)

print(a + b / 3 - 4 * 12)
# can also be written:
print(a + (b / 3) - (4 * 12))

# to get 12:
print((((a + b) / 3) - 4) * 12)
# can also be written this way because of operator prescience
print(((a + b) / 3 - 4) * 12)

c = a + b
d = c / 3
e = d - 4
print(e * 12)

print()
print(a / (b * a) / b)
