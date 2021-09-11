import pygame
import random
from time import time
from math import floor


class Window:
    """Window's class

    Contains functions that affects whole display.

    Fields:
        width : int - width of the window
        height : int - height of the window
        screen : Surface - Surface object from pygame, which is displayed every time"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode([self.width, self.height])

    def build(self):
        """rebuilds field"""
        self.screen = pygame.display.set_mode([self.width, self.height])

    def clear(self):
        """Clear the window and make it gray"""
        self.screen.fill([205, 205, 205])


class Timer:
    """Timer's class

    Class for timer at right top corner of the game.

    Fields:
        screen : Surface - screen, on which timer will be drawed
        img_dict : List[Surface] - list with images for the game
        rect : Rectangle - Rectangle object from pygame for displaying images
        right : int - range between timer's right border and window's right border
        start : float - computer time in seconds when the game started
        event : EventType - EventType object from pygame. Needs to create new Event"""


    def __init__(self, screen, img_dict, start, space, right):
        """Initialize timer's params"""
        self.screen = screen
        self.img_dict = img_dict
        self.rect = img_dict['timer_0'].get_rect()
        self.rect.top = (space - self.rect.height) // 2
        self.right = right
        self.start = start
        self.event = pygame.event.Event(pygame.USEREVENT + 1)

    def draw(self):
        """Draw timer image.

        If value is over 999 then 999 is displayed"""
        curr = floor(time() - self.start)
        if curr > 999:
            curr = 999
        for i in range(3):
            img = self.img_dict['timer_' + str(curr % 10)]
            curr = curr // 10
            self.rect.left = self.right - 10 - self.rect.width * (i + 1)
            self.screen.blit(img, self.rect)

    def reset(self):
        """Reset the timer."""
        self.start = time()
        pygame.time.set_timer(self.event.type, 1000)
        self.draw()


class Counter:
    """Mine counter's class.

    Count amount of mines left to flag.

        screen : Surface - screen, on which counter will be drawed
        img_dict : List[Surface] - list with images for the game
        rect : Rectangle - Rectangle object from pygame for displaying images
        amount : int - initial amount of mines on the field
        length : int - amount of timer poses to be displayed"""

    def __init__(self, screen, img_dict, amount, space):
        """Initialize counter's params"""
        self.screen = screen
        self.img_dict = img_dict
        self.rect = img_dict['timer_0'].get_rect()
        self.rect.top = (space - self.rect.height) // 2
        self.amount = amount
        self.length = max(len(str(amount)), 3)

    def draw(self):
        """Draw counter image.

        If amount of mines left to mark is less than 0, then 0 is displayed.
        There are at least 3 positions at the counter"""
        curr = self.amount
        if curr < 0:
            curr = 0
        for i in range(self.length):
            img = self.img_dict['timer_' + str(curr % 10)]
            curr = curr // 10
            self.rect.left = 10 + self.rect.width * (self.length - i - 1)
            self.screen.blit(img, self.rect)

    def add(self):
        """Add 1 to amount of mines left to mark.

        Also draw counter image."""
        self.amount = self.amount + 1
        self.draw()

    def subtract(self):
        """Subtract 1 from amount of mines left to mark.

        Also draw counter image."""
        self.amount = self.amount - 1
        self.draw()

    def reset(self, amount):
        """Set counter to param value.

        Also draw counter image.

        Parameters
        ----------
        amount: int
            amount of mines on the field"""
        self.amount = amount
        self.draw()


class Player:
    """Class for player and flag buttons.

    Manage game modes by 2 buttons.

    Fields:
        flagging : bool - Statement var, which defines, if the player puts the flag
        game : bool - Statement vat, which defines, if the game is over
        screen : Surface - screen, on which counter will be drawed
        img_dict : List[Surface] - list with images for the game
        player_rect : Rectangle - Rectangle object from pygame. Rectangle object for player button displaying
        flag_rect : Rectangle - Rectangle object from pygame. Rectangle object for flag button displaying
        """
    def __init__(self, window, img_dict, space):
        """Initialize buttons params"""
        self.flagging = False
        self.game = True
        self.screen = window.screen
        self.img_dict = img_dict
        self.player_rect = img_dict['game'].get_rect()
        self.flag_rect = img_dict['checked_flag'].get_rect()
        self.player_rect.left = (window.width + self.player_rect.width) // 2
        self.player_rect.top = (space - self.player_rect.height) // 2
        self.flag_rect.left = window.width // 2 - self.flag_rect.width // 4 * 5
        self.flag_rect.top = (space - self.flag_rect.height) // 2

    def player_draw(self, passed=False):
        """Draw player button image depending on whether the game continues."""
        if self.game:
            self.screen.blit(self.img_dict['game'], self.player_rect)
        else:
            if passed:
                self.screen.blit(self.img_dict['game_passed'], self.player_rect)
            else:
                self.screen.blit(self.img_dict['game_over'], self.player_rect)

    def flag_draw(self):
        """Draw flag button image depending on whether the flags are setting."""
        if self.flagging:
            self.screen.blit(self.img_dict['checked_flag'], self.flag_rect)
        else:
            self.screen.blit(self.img_dict['unchecked_flag'], self.flag_rect)

    def flag_click(self):
        """Process click on the flag button.

        Reverse flagging param.
        If flagging is True, player sets flags on click.
        If flagging is False, player opens cells on click.
        Also draw flag button image."""
        self.flagging = not self.flagging
        self.flag_draw()

    def player_click(self):
        """Precess click on the player button.

        Set game param to True, that means game is not over.
        Also draw player button image."""
        self.game = True
        self.player_draw()


class MinesweeperField:
    """class of the game field.

    Fields:
        screen : Surface - screen, on which counter will be drawed
        img_dict : List[Surface] - list with images for the game
        cell_rect : Rectangle - Rectangle object from pygame. Rectangle object for cells
        v_border_rect : Rectangle - Rectangle object from pygame. Rectangle object for vertical border
        h_border_rect : Rectangle - Rectangle object from pygame. Rectangle object for horizontal border
        sizex : int - width of the field in cells
        sizey : int - height of the field in cells
        cell_width : int - width of the cell in pixels
        cell_height : int - height of the cell in pixels
        width : int - width of the inner part of the field
        height : int - height of the inner part of the field
        full_width : int - full width of the field, including borders
        full_height : int - full height of the field, including borders
        startx : int - horizontal inner part of the field start point in pixels
        starty : int - vertical inner part of the field start point in pixels
        border_startx : int - horizontal outer part of the field start point in pixels
        border_starty : int - vertical outer part of the field start point in pixels
        count : int - the number of mines that should be on the screen
        mined_cells : matrix - True if there is mine, False otherwise.
        checked_cells : matrix - True if cell is checked, False otherwise.
        flagged_cells: matrix - True if there is flag, False otherwise.
        free_cells: matrix - True if there is no mine, False otherwise."""
    def __init__(self, screen, sizex, sizey, count, width, img_dict):
        """Initialize game field params."""
        self.screen = screen
        self.img_dict = img_dict
        self.cell_rect = img_dict[0].get_rect()
        self.v_border_rect = img_dict['v_border'].get_rect()
        self.h_border_rect = img_dict['h_border'].get_rect()
        self.sizex = sizex
        self.sizey = sizey
        self.cell_width = self.cell_rect.width
        self.cell_height = self.cell_rect.height
        self.width = self.cell_width * self.sizex
        self.height = self.cell_height * self.sizey
        self.full_width = self.width + 2 * self.v_border_rect.width
        self.full_height = self.height + 2 * self.h_border_rect.height
        self.startx = (width - self.width)//2
        self.starty = 80 + self.h_border_rect.height
        self.border_startx = self.startx - self.v_border_rect.width
        self.border_starty = self.starty - self.h_border_rect.height
        self.count = count
        self.mined_cells = []
        self.free_cells = []
        self.checked_cells = []
        self.flagged_cells = []

    def gen(self):
        """Generate level."""
        self.fill_cells()
        self.inner_building()
        self.border_building()

    def fill_cells(self):
        """Generate statuses for every cell.

        self.mined_cells : matrix
            True if there is mine, False otherwise.
        self.checked_cells : matrix
            True if cell is checked, False otherwise.
        self.flagged_cells: matrix
            True if there is flag, False otherwise.
        self.free_cells: matrix
            True if there is no mine, False otherwise."""
        self.mined_cells = [[False for j in range(self.sizey)] for i in range(self.sizex)]
        self.checked_cells = [[False for i in range(self.sizey)] for j in range(self.sizex)]
        self.flagged_cells = [[False for i in range(self.sizey)] for j in range(self.sizex)]
        if self.count < 0:
            self.count = self.sizex * self.sizey // 8
        cells = [(i, j) for i in range(self.sizex) for j in range(self.sizey)]
        for i in range(self.count):
            cell = random.randint(0, len(cells) - 1)
            self.mined_cells[cells[cell][0]][cells[cell][1]] = True
            cells.pop(cell)
        self.free_cells = [[not j for j in i] for i in self.mined_cells]

    def inner_building(self):
        """Draw cells for current size."""
        cell_rect = self.cell_rect
        for i in range(self.sizex):
            for j in range(self.sizey):
                cell_rect.left = self.startx + cell_rect.width * i
                cell_rect.top = self.starty + cell_rect.height * j
                self.screen.blit(self.img_dict['unpressed_button'], cell_rect)  # '''random.randint(0,8)],cell_rect)

    def border_building(self):
        """Draw borders for current size."""
        cell_rect = self.cell_rect
        h_border_rect = self.h_border_rect
        v_border_rect = self.v_border_rect
        corner_rect = self.img_dict['right_top_corner'].get_rect()
        for i in range(self.sizex):
            h_border_rect.left = self.startx + cell_rect.width * i
            h_border_rect.top = self.border_starty
            self.screen.blit(self.img_dict['h_border'], h_border_rect)
            h_border_rect.top = self.starty + self.height
            self.screen.blit(self.img_dict['h_border'], h_border_rect)
        for j in range(self.sizey):
            v_border_rect.left = self.border_startx
            v_border_rect.top = self.starty + j * cell_rect.height
            self.screen.blit(self.img_dict['v_border'], v_border_rect)
            v_border_rect.left = self.startx + self.width
            self.screen.blit(self.img_dict['v_border'], v_border_rect)
        corner_rect.left, corner_rect.top = self.border_startx, self.border_starty
        self.screen.blit(self.img_dict['left_top_corner'], corner_rect)
        corner_rect.left = self.startx + self.width
        self.screen.blit(self.img_dict['right_top_corner'], corner_rect)
        corner_rect.top = self.starty + self.height
        self.screen.blit(self.img_dict['right_bottom_corner'], corner_rect)
        corner_rect.left = self.border_startx
        self.screen.blit(self.img_dict['left_bottom_corner'], corner_rect)

    def open_cell(self, x, y):
        """Open cell and draw it's content.

        :return: False if there was mine and True otherwise."""
        if (x >= 0) and (y >= 0) and (x < self.sizex) and (y < self.sizey) \
                and (not self.checked_cells[x][y]) and (not self.flagged_cells[x][y]):
            self.checked_cells[x][y] = True
            if self.mined_cells[x][y]:
                return False
            else:
                self.draw_cell(x, y)
        return True

    def flag_cell(self, x, y):
        """Set flag status.

        Sets True if it was False and False if it was True.
        All cells are False at the start"""
        if (x >= 0) and (y >= 0) and (x < self.sizex) and (y < self.sizey) and (not self.checked_cells[x][y]):
            self.flagged_cells[x][y] = not self.flagged_cells[x][y]
            self.draw_cell(x, y)

    def draw_cell(self, x, y):
        """Draw cell depending on it's status."""
        cell_rect = self.cell_rect
        cell_rect.left = self.startx + x * self.cell_width
        cell_rect.top = self.starty + y * self.cell_height
        if self.checked_cells[x][y]:
            if self.free_cells[x][y]:
                count = 0
                for i in range(x - 1, x + 2):
                    for j in range(y - 1, y + 2):
                        if (i >= 0) and (j >= 0) and (i < self.sizex) and (j < self.sizey) and (self.mined_cells[i][j]):
                            count = count + 1
                self.screen.blit(self.img_dict[count], cell_rect)
                if count == 0:
                    for i in range(x - 1, x + 2):
                        for j in range(y - 1, y + 2):
                            if (i >= 0) and (j >= 0) and (i < self.sizex) and (j < self.sizey) \
                                    and (not self.checked_cells[i][j]):
                                self.open_cell(i, j)
        else:
            if self.flagged_cells[x][y]:
                self.screen.blit(self.img_dict['flag'], cell_rect)
            else:
                self.screen.blit(self.img_dict['unpressed_button'], cell_rect)

    def draw_mines(self):
        """Draw every mine at the field.

        Draw mines if cells are not opened and not flagged."""
        cell_rect = self.cell_rect
        for i in range(self.sizex):
            for j in range(self.sizey):
                if self.mined_cells[i][j] and not self.flagged_cells[i][j]:
                    cell_rect.left = self.startx + self.cell_width * i
                    cell_rect.top = self.starty + self.cell_height * j
                    if self.checked_cells[i][j]:
                        self.screen.blit(self.img_dict['pressed_mine'], cell_rect)
                    else:
                        self.screen.blit(self.img_dict['mine'], cell_rect)


class Minesweeper:
    """Game class.

    Main game class, that constains minesweeper's code.

    Fields:
        img_dict : List[Surface] - list with images for the game
        field : MinesweeperField - field for the game
        player : Player - game status and status buttons class
        counter : Counter - mine counter for the game
        timer : Timer - timer counting the time from the start of the game
        in_game : bool - boolean var, which defines, if the window was closed"""

    def __init__(self, sizex, sizey, count=0):
        """Initialize everything needed and starts the game."""
        pygame.init()
        self.img_dict = self.img_init()
        cell_rect = self.img_dict[0].get_rect()
        v_border_rect = self.img_dict['v_border'].get_rect()
        h_border_rect = self.img_dict['h_border'].get_rect()
        field_width = cell_rect.width * max(sizex, 10) + v_border_rect.width * 2 + 20
        field_height = cell_rect.height * sizey + h_border_rect.height * 2 + 100
        window = Window(field_width, field_height)
        window.clear()
        count = min(abs(count), sizex * sizey)
        self.field = MinesweeperField(window.screen, sizex, sizey, count, field_width, self.img_dict)
        self.field.gen()
        self.player = Player(window, self.img_dict, self.field.border_starty)
        self.player.player_draw()
        self.player.flag_draw()
        self.counter = Counter(window.screen, self.img_dict, self.field.count, self.field.border_starty)
        self.counter.draw()
        self.timer = Timer(window.screen, self.img_dict, time(), self.field.border_starty, window.width)
        pygame.time.set_timer(self.timer.event.type, 1000)
        self.timer.draw()
        self.in_game = True
        pygame.display.flip()

    @staticmethod
    def img_init():
        """Load images for the game

        :return: dictionary of every image in the game"""
        img_dict = {
            0: pygame.image.load("imgs/pressed_button_0.jpg"),
            1: pygame.image.load("imgs/pressed_button_1.jpg"),
            2: pygame.image.load("imgs/pressed_button_2.jpg"),
            3: pygame.image.load("imgs/pressed_button_3.jpg"),
            4: pygame.image.load("imgs/pressed_button_4.jpg"),
            5: pygame.image.load("imgs/pressed_button_5.jpg"),
            6: pygame.image.load("imgs/pressed_button_6.jpg"),
            7: pygame.image.load("imgs/pressed_button_7.jpg"),
            8: pygame.image.load("imgs/pressed_button_8.jpg"),
            'unpressed_button': pygame.image.load("imgs/unpressed_button.jpg"),
            'mine': pygame.image.load("imgs/mine.jpg"),
            'pressed_mine': pygame.image.load("imgs/pressed_mine.jpg"),
            'flag': pygame.image.load("imgs/flag.jpg"),
            'h_border': pygame.image.load("imgs/horizontal_border.jpg"),
            'v_border': pygame.image.load("imgs/vertical_border.jpg"),
            'right_top_corner': pygame.image.load("imgs/right_top_corner.jpg"),
            'right_bottom_corner': pygame.image.load("imgs/right_bottom_corner.jpg"),
            'left_top_corner': pygame.image.load("imgs/left_top_corner.jpg"),
            'left_bottom_corner': pygame.image.load("imgs/left_bottom_corner.jpg"),
            'timer_0': pygame.image.load("imgs/timer_0.jpg"),
            'timer_1': pygame.image.load("imgs/timer_1.jpg"),
            'timer_2': pygame.image.load("imgs/timer_2.jpg"),
            'timer_3': pygame.image.load("imgs/timer_3.jpg"),
            'timer_4': pygame.image.load("imgs/timer_4.jpg"),
            'timer_5': pygame.image.load("imgs/timer_5.jpg"),
            'timer_6': pygame.image.load("imgs/timer_6.jpg"),
            'timer_7': pygame.image.load("imgs/timer_7.jpg"),
            'timer_8': pygame.image.load("imgs/timer_8.jpg"),
            'timer_9': pygame.image.load("imgs/timer_9.jpg"),
            'checked_flag': pygame.image.load("imgs/checked_flag.jpg"),
            'unchecked_flag': pygame.image.load("imgs/unchecked_flag.jpg"),
            'game': pygame.image.load("imgs/game.jpg"),
            'game_over': pygame.image.load("imgs/game_over.jpg"),
            'game_passed': pygame.image.load("imgs/game_passed.jpg"),
        }
        return img_dict

    def update(self, event_list):
        """Process events."""
        for event in event_list:
            if event.type == pygame.QUIT:  # processing pressing on the cross
                self.in_game = False
            elif event.type == self.timer.event.type:  # processing timer
                self.timer.draw()
                pygame.display.flip()
            elif pygame.mouse.get_pressed()[0] and (event.type == pygame.MOUSEBUTTONDOWN):  # processing game logic on click
                self.game_logic()
                pygame.display.flip()

    def game_logic(self, x=-1, y=-1):
        """Process game logic."""
        if (x == -1) and (y == -1):
            x, y = pygame.mouse.get_pos()
        check = False
        if self.player.game:  # processing click on field
            if (x < self.field.startx + self.field.width) and (y < self.field.starty + self.field.height) \
                    and (x > self.field.startx) and (y > self.field.starty):
                x = (x - self.field.startx) // self.field.cell_width
                y = (y - self.field.starty) // self.field.cell_height
                if self.player.flagging:
                    self.field.flag_cell(x, y)
                    if not self.field.checked_cells[x][y]:
                        if self.field.flagged_cells[x][y]:
                            self.counter.subtract()
                        else:
                            self.counter.add()
                else:
                    self.player.game = self.field.open_cell(x, y)
                    check = True
                    if not self.player.game:
                        self.player.player_draw()
                        self.field.draw_mines()
                        pygame.time.set_timer(self.timer.event.type, 0)
                if (self.field.flagged_cells == self.field.mined_cells) or\
                        (self.field.checked_cells == self.field.free_cells and check):
                    self.player.game = False
                    self.player.player_draw(True)
                    self.field.draw_mines()
                    pygame.time.set_timer(self.timer.event.type, 0)
        game_rect = self.player.player_rect
        if (x >= game_rect.left) and (y >= game_rect.top) and (x <= game_rect.left + game_rect.width) \
                    and (y <= game_rect.top + game_rect.height):  # processing click on player button
                self.player.player_click()
                self.field.gen()
                self.timer.reset()
                self.counter.reset(self.field.count)
        flag_rect = self.player.flag_rect
        if (x >= flag_rect.left) and (y >= flag_rect.top):  # processing click on flag button
            if (x <= flag_rect.left + flag_rect.width) and (y <= flag_rect.top + flag_rect.height):
                self.player.flag_click()

    def play(self):
        """Main cycled function that generates events while the game is not closed.

        When user close game window, program goes back to menu"""
        while self.in_game:
            event_list = pygame.event.get()
            if event_list:
                self.update(event_list)


if __name__ == '__main__':
    game = Minesweeper(10, 10, count=20)
    game.play()