# In this file, you have two classes, Card and Deck.

# Both have been set up with some basic methods (constructors, and a couple of dunder methods)

# Deck has two methods which need completing - shuffle and deal.

# With these methods, you should be able to create almost any card game which you can think of!

# We recommend having a go at implementing one of:
# - snap (easiest)
# - blackjack (easy scoring)
# - baccarat (slightly harder scoring)
# - poker (more difficult)

# If you have another card game you want to implement - go for it!

# You can edit/add to/change these classes as you need to.


import random


class Card:
    """
    Class to represent a single playing card.
    """

    def __init__(self, rank, suit):
        """
        Creates a playing card with the given rank & suit.
        """
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    """
    Class to represent a deck of playing cards.
    """

    SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

    RANKS = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]

    def __init__(self):
        """
        Creates a full deck of cards.
        """
        self.deck = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.deck.append(Card(rank, suit))

    def shuffle(self):
        """Shuffles this deck randomly."""
        # NEEDS COMPLETING

    def deal(self):
        """Removes top card from this deck and returns it."""
        # NEEDS COMPLETING

    def __len__(self):
        return len(self.deck)

    def __str__(self):
        return "\n".join(str(c) for c in self.deck)


# Implement a card game!
