print("Hello")
print('Python is fun')
print("Python's string are easy to use")
# can use "quotes" inside strings if you use ''
print('We can even include "quotes" in strings')
print("hello" + " world")

# strings as variables
greeting = "hello"
name = input("Please enter your name ")
print(greeting + ' ' + name)

age = 24
print(age)

# identifies object type
print(type(greeting))
print(type(age))

# can change variable type later
age = "2 years"
print(age)
print(type(age))

# more clear if you use age_in_years
age2 = 4
age2_in_years = "4 years"
print(name + " is " + age2 + " years old")
print(type(age2))
