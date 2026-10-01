# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}") # prints the original string
print(f"Modified String 1: {user_string.lower()}") # prints the original string in lower case
print(f"Modified String 2: {user_string.upper()}") # prints the orignal string in upper case
print(f"Modified String 3: {user_string.strip()}") # prints the original string with starting and ending white space removed
print(f"Modified String 4: {user_string.replace('a', '@')}") # prints the original string with a replaced with @
print(f"Modified String 5: {user_string.capitalize()}") # prints the original string with the first letter capitalized
print(f"Modified String 6: {user_string[::-1]}") # prints the string in reverse order
print(f"Modified String 7: {user_string.title()}") # prints the original string with title case
print(f"Modified String 8: {len(user_string)}") # prints the number of characters in the string
print(f"Modified String 9: {user_string.find('a')}") # prints the number of characters from the start until the first 'a' is found
print(f"Modified String 10: {user_string.count('a')}") # prints the number of 'a's in the string
print(f"Modified String 11: {user_string.startswith('Hello')}") # prints a boolean statement on whether the first word is 'Hello'
print(f"Modified String 12: {user_string.endswith('!')}") # prints a boolean statement on whether the last character is '!'
print(f"Modified String 13: {user_string.isalnum()}") # prints a boolean statement on whether the string is alpha-numeric (no whitespace) 
print(f"Modified String 14: {user_string.isalpha()}") # prints a boolean statement on whether the string is solely alphabetical (no whitespace)
print(f"Modified String 15: {user_string.isdigit()}") # prints a boolean statement on whether the string solely contains digits



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!