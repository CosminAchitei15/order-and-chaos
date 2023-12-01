from texttable import Texttable


class Board:
    def __init__(self):
        self._board = [["" for i in range(6)] for j in range(6)]

    @property
    def board(self):
        return self._board

    def __str__(self):
        t = Texttable()

        for i in range(6):
            line = []
            for j in range(6):
                line.append(self._board[i][j])
            t.add_row(line)

        return t.draw()