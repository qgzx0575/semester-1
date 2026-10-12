# Week 1.3, Session 1: For loop equivalent to a list comprehension

animals = ['dog','cat','goldfish','hamster']

not_fish = [item for item in animals if item != 'goldfish']

print(not_fish)


# write the equivalent for loop to create the not_fish list from animals
# print your result to verify it is the same

not_fish_2 = []

for item in animals[:]:
    if item != "goldfish":
        not_fish_2.append(item)
    else:
        animals.remove(item)

print(not_fish_2)