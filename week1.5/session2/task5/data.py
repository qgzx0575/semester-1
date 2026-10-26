# Week 1.5, Session 2: Task 5

class Dataset:
    """
    A numeric dataset, loaded from a file.
    """

    def __init__(self, filename=None):
        """
        Creates a Dataset containing data from the specified file.

        If no file is specified, an empty Dataset is created.
        """
        self.data = []
        if filename:
            self.load_data(filename)

    def load_data(self, filename):
        """
        Loads data from the specified file into this Dataset.

        Any existing data will be deleted.
        """

    def __len__(self):
        """
        Returns the size of this Dataset.
        """

    def __getitem__(self, index):
        """
        Returns the value at the specified position in this Dataset.
        """

    def mean(self):
        """
        Returns the arithmetic mean of the values in this Dataset.
        """

    def median(self):
        """
        Returns the median of the values in this Dataset.
        """
