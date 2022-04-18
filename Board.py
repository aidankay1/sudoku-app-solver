from copy import deepcopy


class Board:
    initial_board = [[0] * 9 for _ in range(9)]
    solved_board = []

    def fill(self, n: int, row: int, col: int):
        self.initial_board[row][col] = n
        # A more efficient implementation would extract the below step into its own method so it only runs once
        self.solved_board = deepcopy(self.initial_board)

    def print(self):
        for row in self.solved_board:
            print(row)

    def solve(self) -> bool:
        # Inspired by Coding with John (https://youtu.be/mcXc8Mva2bA)
        def _exists_in_row(self, n: int, row: int) -> bool:
            for i in range(9):
                if self.solved_board[row][i] == n:
                    return True
            return False

        def _exists_in_column(self, n: int, col: int) -> bool:
            for i in range(9):
                if self.solved_board[i][col] == n:
                    return True
            return False

        def _exists_in_square(self, n: int, row: int, col: int) -> bool:
            square_origin_row = row - (row % 3)
            square_origin_col = col - (col % 3)

            for i in range(square_origin_row, square_origin_row + 3):
                for j in range(square_origin_col, square_origin_col + 3):
                    if self.solved_board[i][j] == n:
                        return True
            return False

        def _is_valid_placement(self, n: int, row: int, col: int) -> bool:
            return not (
                _exists_in_row(self, n, row)
                or _exists_in_column(self, n, col)
                or _exists_in_square(self, n, row, col)
            )

        for row in range(9):
            for col in range(9):
                if self.solved_board[row][col] == 0:
                    for number_to_try in range(1, 10):
                        if _is_valid_placement(self, number_to_try, row, col):
                            self.solved_board[row][col] = number_to_try

                            if self.solve():
                                return True

                            self.solved_board[row][col] = 0
                    return False
        return True
