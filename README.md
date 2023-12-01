# Order and Chaos

A python  implementation of the game 
"Order and Chaos" that uses layered architecture, 
file read-write operations and OOP concepts.

## 1. Rules of the game

Both Order (the player) and Chaos (the computer)
control Xs and Os. Order aims to get five Xs or 5 Os
in a row, either horizontally, vertically or
diagonally, while Chaos endeavors to prevent this.
If 5 like pieces in a row are placed Order wins,
and if the board is filled by symbols without
Order winning then Chaos is the winner.

## 2. Save feature

At any point in the game, while it's your turn,
typing "save" will save the current board to
file.txt. When starting up the program, you can
choose between loading the board that is currently
in file.txt by typing "load", or you can start up
a new game by writing "start".

## 3. Installation

* clone this repository
* pip install texttable
* cd into the file and use python3 main.py

## 4. Final thoughts

This project was made during my 
"Fundamentals of Programming" course in my
first semester of college, and it represents
the beginning of my journey in CS. 