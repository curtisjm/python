# next line
splitString = "This string has been\nsplit over\nseveral\nlines"
print(splitString)

# tab
tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

# quotes in strings
print('The pet shop owner said "No, no, \'e\'s uh...he\'s resting."')
# or
print("The pet shop owner said \"No, no, 'e's uh...he's resting.\"")
# or
print("""The pet shop owner said "No, no, no 'e's uh...he's resting". """)

# \ escapes the strings from bring printed over several lines
anotherSplitString = """This string has been \
split over \
several \
lines"""
print(anotherSplitString)

# escape backslash characters with \ so tabs and notes don't have errors
print("C:\\Users\\timbuchalka\\notes.txt")
# raw string with r in front
print(r"C:\Users\timbuchalka\notes.txt")
