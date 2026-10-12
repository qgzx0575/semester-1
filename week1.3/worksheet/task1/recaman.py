# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'
sequence = []
num = 0

for i in range(L):
    if sequence.count(num - i) == 0 and num - i > 0: # checks if should be subtracted
        num -= i
    else:
        num += i
    sequence.append(num)
    print(num)


# You may wish to use further output for testing purposes while you develop your code

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence