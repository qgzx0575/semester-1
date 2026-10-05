# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)
albums = {
    "underscores": ["fishmonger", "Wallsocket", "U"],
    "Kanye West": ["The College Dropout", "Late Registration", "Graduation"],
    "Lil Uzi Vert": ["Luv is Rage", "Eternal Atake", "Luv is Rage 2"],
    "Rihanna": ["Good Girl Gone Bad", "Unapologetic", "ANTI"]
}

# Pretty-print the data structure
pprint(albums)
# Display details of one album recorded by a specific artist
specificAlbum = albums.get(input("Insert the artist: "))
num = int(input("Insert the number: "))
print(specificAlbum[num-1])