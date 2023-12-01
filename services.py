from domain import *
from repo import *
import random


class Services:
    def __init__(self, repo: TextFile, board: Board):
        self._board = board
        self._repo = repo

    def printBoard(self):
        return str(self._board)

    def makeMove(self, row, col, marker):
        """

        :param row: the row I want my marker on
        :param col: the column I want my marker on
        :param marker: the marker
        :return: puts the marker on said position if the marker is correct, the position is on the board and the position is empty
        """
        if 0 <= row - 1 <= 5 and 0 <= col - 1 <= 5 and (marker == "X" or marker == "O") and self._board.board[row-1][col-1] == "":
            self._board.board[row - 1][col - 1] = marker
        else:
            raise ValueError

    def aiMove(self):
        """
        this function randomly chooses a valid row, col and marker for the AI to place, and places it if the position is
        empty
        :return:
        """
        row = random.randint(0, 5)
        col = random.randint(0, 5)
        marker = random.choice(["X", "O"])
        ok = 0
        while ok == 0:
            if self._board.board[row][col] == "":
                ok = 1
                self._board.board[row][col] = marker
            else:
                row = random.randint(0, 5)
                col = random.randint(0, 5)
                marker = random.choice(["X", "O"])

    def chaosWinCondition(self):
        """
        Chaos wins if the board has no empty spaces without Order winning
        :return:
        """
        ok = 1
        for i in range(6):
            for j in range(6):
                if self._board.board[i][j] == "":
                    ok = 0
        if ok == 1:
            return True
        return False

    def orderWinCondition(self):
        """
        Order wins if there are 5 of the same marker on same line, column or diagonal
        :return:
        """
        ok = 0
        # Verify for lines
        for i in range(6):
            if self._board.board[i][0] == self._board.board[i][1] == self._board.board[i][2] == self._board.board[i][3] == self._board.board[i][4] != "":
                ok = 1
            elif self._board.board[i][1] == self._board.board[i][2] == self._board.board[i][3] == self._board.board[i][4] == self._board.board[i][5] != "":
                ok = 1

        # Verify for columns
        for j in range(6):
            if self._board.board[0][j] == self._board.board[1][j] == self._board.board[2][j] == self._board.board[3][j] == self._board.board[4][j] != "":
                ok = 1
            elif self._board.board[1][j] == self._board.board[2][j] == self._board.board[3][j] == self._board.board[4][j] == self._board.board[5][j] != "":
                ok = 1

        # Verify for 1st diagonal
        if self._board.board[0][0] == self._board.board[1][1] == self._board.board[2][2] == self._board.board[3][3] == \
                self._board.board[4][4] != "":
            ok = 1
        elif self._board.board[1][1] == self._board.board[2][2] == self._board.board[3][3] == self._board.board[4][4] == \
                self._board.board[5][5] != "":
            ok = 1

        # Verify for 2nd diagonal
        elif self._board.board[0][5] == self._board.board[1][4] == self._board.board[2][3] == self._board.board[3][2] == \
                self._board.board[4][1] != "":
            ok = 1
        elif self._board.board[1][4] == self._board.board[2][3] == self._board.board[3][2] == self._board.board[4][1] == \
                self._board.board[5][0] != "":
            ok = 1
        if ok == 1:
            return True
        return False

    def addToFile(self):
        self._repo.add(self._board.board)

    def loadFromFile(self):
        self._board = self._repo.get(-1)