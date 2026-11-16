import random

# Options for random number generation:

print("Random integer:", random.randint(0, 10000))
print("Random float:", random.random())

# Using random with collections:

print("\nShuffling a list of 10 integers:")

nums = list(range(10))
print(nums)

random.shuffle(nums)
print(nums)

print("\nChoosing from a list of 1000 integers:")

nums = list(range(1000))

one_random = random.choice(nums)
print("1 value:", one_random)

selection = random.choices(nums, k=10)
print("10 values:", selection)
