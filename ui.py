from domain import *
from repo import *
from services import *


class UI:
    def __init__(self, serv: Services):
        self._serv = serv

    def Startup(self):
        print("Type load to load the last save or start to start a new game!")
        inp = input(">")
        if inp == "load":
            self._serv.loadFromFile()
        if inp != "load" and inp != "start":
            print("Invalid input!")
            return 0
        print(self._serv.printBoard())
        endgame = 0
        while endgame == 0:
            print("Order's turn! <row>,<column>,<marker> or type save to save the current game instance")
            move = input(">")
            if move == "save":
                self._serv.addToFile()
                print("Game saved!")
                break
            else:
                mov = move.split(",")
                try:
                    self._serv.makeMove(int(mov[0]), int(mov[1]), str(mov[2]))
                except ValueError:
                    print("Invalid input!")
                if self._serv.orderWinCondition():
                    print(self._serv.printBoard())
                    print("Order won!")
                    break
                if self._serv.chaosWinCondition():
                    print(self._serv.printBoard())
                    print("Chaos won!")
                    break
                print(self._serv.printBoard())

            print("Chaos's turn! ")
            try:
                self._serv.aiMove()
            except ValueError:
                print("Invalid input!")
            if self._serv.orderWinCondition():
                print("Order won!")
                break
            if self._serv.chaosWinCondition():
                print("Chaos won!")
                break
            print(self._serv.printBoard())
