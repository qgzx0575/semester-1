# Week 1.3, Session 2: Write User Information to a File


# Prompt the user for their name, age, and favorite colour.

# Open a file called 'user_info.txt' for reading

# Write each piece of information to the file, each on a new line.

# Hints:
# - Remember to add \n for new lines when writing to files


# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'

with open("user_info.txt", "a") as file:
    userName = input("Enter the names, separated by spaces: ").split()
    userAge = input("Enter the ages, separated by spaces: ").split()
    userColor = input("Enter the favorite colors, separated by spaces: ").split()
    if len(userName) == len(userAge) == len(userColor):
        [file.write(f"{userName[i]},{userAge[i]},{userColor[i]}\n") for i in range(len(userName))]
    else:
        print("Sorry, an entry was submitted incorrectly.")

