# Tests unitaires (exemple)
import unittest
from game.board import Board
from game.keeper import Keeper

class TestBoard(unittest.TestCase):
    def test_init(self):
        self.assertTrue(True)

    def test_place_and_move_keeper(self):
        board = Board(3, 3)
        keeper = Keeper("TestKeeper")
        board.place_keeper(keeper, 1, 1)
        self.assertEqual((keeper.x, keeper.y), (1, 1))
        board.move_keeper(keeper, 2, 2)
        self.assertEqual((keeper.x, keeper.y), (2, 2))
        self.assertIs(board.tiles[2][2], keeper)

if __name__ == "__main__":
    unittest.main()
