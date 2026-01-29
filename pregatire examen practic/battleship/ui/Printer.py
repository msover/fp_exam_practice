from data.PositionState import PositionState


class Printer:

    @staticmethod
    def printBoard(board: list[list[PositionState]]):
        print(end="  ")
        for col in range(6):
            print(chr(65+col), end=" ")
        print()
        for row in range(6):
            print(row, end=" ")
            for col in range(6):
                print(board[row][col].value, end=" ")
            print()