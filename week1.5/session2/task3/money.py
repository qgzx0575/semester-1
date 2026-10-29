# Week 1.5, Session 2: Task 3

class Money:
    """
    An amount of money, in British Pounds Sterling.
    """

    def __init__(self, pounds, pence):
        """
        Creates a Money object, given the number of pounds and pence.
        """
        # Add validation code here, to check that
        # - the pounds parameter is an integer
        # - pounds is not negative
        # - the pence parameter is an integer
        # - pence is not negative and not greater than 99
        # Raise appropriate exceptions if any of these are violated
        if not (isinstance(pounds, int) and isinstance(pence, int)):
            raise TypeError("Value is not an integer.")
        elif pounds<0 or not 0<pence<100:
            raise TypeError("Value is not within bounds.")
        self.pounds = pounds
        self.pence = pence

    def __str__(self):
        """
        Returns a string representation of this Money.
        """
        # Add code here to return an appropriate string representation
        # Use the currency symbol for British Pounds Sterling
        # Represent pence with a leading zero if needed (e.g. '05')
        return f"£{self.pounds}.{self.pence:02d}"

    def __add__(self, other):
        """
        Adds this Money to another Money, returning the total.
        """
        total_pence = self.pence+other.pence
        total_pounds = self.pounds+other.pounds+total_pence//100
        remaining_pence = total_pence % 100
        return Money(total_pounds, remaining_pence)

