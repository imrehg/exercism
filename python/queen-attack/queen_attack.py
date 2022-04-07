class Queen:
    def __init__(self, row: int, column: int) -> None:
        if row < 0:
            raise ValueError("row not positive")
        if row > 7:
            raise ValueError("row not on board")
        if column < 0:
            raise ValueError("column not positive")
        if column > 7:
            raise ValueError("column not on board")

        self.row = row
        self.column = column

    def can_attack(self, another_queen: "Queen") -> bool:
        """Check if queens can attack each other.

        Attack is possible if they are on the same row,
        same column, or along the diagonals.
        """
        row_offset = abs(self.row - another_queen.row)
        column_offset = abs(self.column - another_queen.column)
        if row_offset == column_offset == 0:
            raise ValueError(
                "Invalid queen position: both queens in the same square"
            )
        return (
            row_offset == 0
            or column_offset == 0
            or row_offset == column_offset
        )
