import unittest
import pygame
from Minesweeper import Minesweeper
from main import Button, Window


class MyTestCase(unittest.TestCase):

    def test_full_filled(self):
        minesweeper = Minesweeper(10, 10, 100)
        self.assertEqual(minesweeper.field.mined_cells, [[True for i in range(10)] for j in range(10)])

    def test_empty(self):
        minesweeper = Minesweeper(10, 10, 0)
        self.assertEqual(minesweeper.field.mined_cells, [[False for i in range(10)] for j in range(10)])

    def test_open_empty_cell(self):
        minesweeper = Minesweeper(2, 2, 0)
        minesweeper.field.mined_cells = [[True, False], [True, False]]
        self.assertEqual(minesweeper.field.open_cell(1, 1), True)

    def test_open_mined_cell(self):
        minesweeper = Minesweeper(2, 2, 0)
        minesweeper.field.mined_cells = [[True, False], [True, False]]
        self.assertEqual(minesweeper.field.open_cell(1, 0), False)

    def test_flag_button_test(self):
        minesweeper = Minesweeper(2, 2, 0)
        minesweeper.game_logic(140, 40)
        self.assertEqual(minesweeper.player.flagging, True)
        minesweeper.game_logic(140, 40)
        self.assertEqual(minesweeper.player.flagging, False)

    def test_player_button_test(self):
        minesweeper = Minesweeper(2, 2, 4)
        self.assertEqual(minesweeper.player.game, True)
        minesweeper.player.game = False
        minesweeper.game_logic(250, 40)
        self.assertEqual(minesweeper.player.game, True)

    def test_click_on_mined_cell(self):
        minesweeper = Minesweeper(2, 2, 4)
        self.assertEqual(minesweeper.player.game, True)
        minesweeper.game_logic(200, 120)
        self.assertEqual(minesweeper.player.game, False)

    def test_click_away_from_everything(self):
        minesweeper = Minesweeper(2, 2, 4)
        save_player = minesweeper.player
        save_field = minesweeper.field
        save_counter = minesweeper.counter
        minesweeper.game_logic(200, 20)
        self.assertEqual(save_player, minesweeper.player)
        self.assertEqual(save_field, minesweeper.field)
        self.assertEqual(save_counter, minesweeper.counter)

    def test_click_on_button(self):
        window = Window(300, 300)
        button = Button(0, 1, pygame.Rect(0, 0, 50, 50), window)
        self.assertEqual(button.check_click(150, 150), True)

    def test_click_on_button_border(self):
        window = Window(300, 300)
        button = Button(0, 1, pygame.Rect(0, 0, 50, 50), window)
        self.assertEqual(button.check_click(125, 150), False)
        self.assertEqual(button.check_click(150, 125), False)
        self.assertEqual(button.check_click(150, 175), False)
        self.assertEqual(button.check_click(175, 150), False)

    def test_click_far_away_from_button(self):
        window = Window(300, 300)
        button = Button(0, 1, pygame.Rect(0, 0, 50, 50), window)
        self.assertEqual(button.check_click(0, 150), False)
        self.assertEqual(button.check_click(150, 0), False)
        self.assertEqual(button.check_click(300, 0), False)
        self.assertEqual(button.check_click(0, 300), False)


if __name__ == '__main__':
    unittest.main()
