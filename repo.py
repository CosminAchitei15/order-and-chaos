from domain import *


class TextFile:
    def __init__(self):
        self._data = []
        self._loadfromfile()

    def _loadfromfile(self):
        fin = open("file.txt", "rt")

        lines = fin.readlines()
        for l in lines:
            self._data.append(l.split())

        fin.close()

    def _writetofile(self):
        fout = open("file.txt", "wt")

        for board in self._data:
            fout.write(str(board) + '\n')

        fout.close()

    def getall(self):
        return self._data

    def add(self, board: Board):
        self._data.append(board)
        self._writetofile()

    def get(self, index):
        return self._data[index]