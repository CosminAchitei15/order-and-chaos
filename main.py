from domain import *
from repo import *
from services import *
from ui import *

board = Board()
repo = TextFile()
services = Services(repo, board)
ui = UI(services)

ui.Startup()
