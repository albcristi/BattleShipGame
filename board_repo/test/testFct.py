

from board_repo.board_repository import *

def tst():
    board = Board()
    print(board.str())
    assert board.battleship_shape(2,2,'vertical') == [[2, 2], [3, 2], [4, 2], [5, 2]]
    assert board.cruiser_shape(2,2,'vertical') == [[2, 2], [3, 2], [4, 2]]
    assert board.destroyer_shape(2,2,'vertical') == [[2, 2], [3, 2]]

tst()