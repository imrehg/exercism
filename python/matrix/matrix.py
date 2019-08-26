"""Storing and processing a matrix of numbers"""

class Matrix():
    """
    Matrix contains a matrix of integers
    """

    def __init__(self, matrix_string):
        """
        Initializing the given matrix

        Args:
            matrix_string: matix items, separated by space
                within the row, newline within the column.
                The items are assumed to be integers encoded
                in the string.
        """
        self.matrix = [[int(n) for n in row.split()] for row in matrix_string.splitlines()]

    def row(self, index):
        """
        Fetch the items of the matrix in a given row.

        Args:
            index: row index, 1-based

        Returns:
            List of items as integers in the given row.
        """
        return self.matrix[index-1].copy()

    def column(self, index):
        """
        Fetch the items of the matrix in a given column.

        Args:
            index: column index, 1-based

        Returns:
            List of items as integers in the given column.
        """
        return [row[index - 1] for row in self.matrix]
