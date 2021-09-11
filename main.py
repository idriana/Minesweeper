from Minesweeper import Minesweeper, Window
import pygame
import sys


class Button:
    """Menu button class

    Fields:
        id : int - number of the button in menu
        screen : Surface - screen, on which counter will be drawed
        rect : Rectangle - Rectangle object from pygame. Rectangle object for button displaying"""
    def __init__(self, id, amount, rect, window):
        self.id = id
        self.screen = window.screen
        self.rect = rect
        self.rect.left = (window.width - self.rect.width)//2
        self.rect.top = ((window.height - amount * self.rect.height)//(amount + 1) * (id + 1)) + (self.rect.height * id)

    def check_click(self, x=-1, y=-1):
        """Function to check if button has been pressed

        can get x, y, simulating clicking
        if x and y are undefined, reads mouse pos"""
        if (x == -1) and (y == -1):
            x, y = pygame.mouse.get_pos()
        if (x > self.rect.left) and (x < self.rect.left + self.rect.width) and \
                (y > self.rect.top) and (y < self.rect.top + self.rect.height):
            return True
        return False

    def draw(self, image):
        """draw button image

        gets image as param"""
        self.screen.blit(image, self.rect)


class Menu:
    """Menu class

    in menu player can click on 3 buttons:
    start - to start the game
    difficulty button (easy/medium/hard) - to pick difficulty
    exit - to close the app

    Fields:
        window : Window - window, in which application works
        screen : Surface - screen, on which counter will be drawed
        img_dict : List[Surface] - list with images for the game
        diff_dict : dict - difficulty dictionary for easier coding
        difficulty : str - current difficulty level
        start_button : Button - first button in menu, which starts the game
        difficulty_button : Button - second button in menu, which defines difficulty level of the game
        exit_button : Button - the last button in menu, which exits the game
        minesweeper : Minesweeper - game object"""
    def __init__(self):
        self.window = Window(300, 300)
        self.window.clear()
        self.screen = self.window.screen
        self.img_dict = self.image_init()
        self.diff_dict = self.difficulty_init()
        self.difficulty = "easy"
        self.start_button = Button(0, 3, self.img_dict["start"].get_rect(), self.window)
        self.difficulty_button = Button(1, 3, self.img_dict["easy"].get_rect(), self.window)
        self.exit_button = Button(2, 3, self.img_dict["exit"].get_rect(), self.window)
        self.start_button.draw(self.img_dict["start"])
        self.difficulty_button.draw(self.img_dict[self.difficulty])
        self.exit_button.draw(self.img_dict["exit"])
        self.minesweeper = None
        pygame.display.flip()

    @staticmethod
    def image_init():
        """initialize pictures for menu"""
        img_dict = {
            "start": pygame.image.load("imgs/play_button.jpg"),
            "easy": pygame.image.load("imgs/easy.jpg"),
            "medium": pygame.image.load("imgs/medium.jpg"),
            "hard": pygame.image.load("imgs/hard.jpg"),
            "exit": pygame.image.load("imgs/exit_button.jpg")
        }
        return img_dict

    @staticmethod
    def difficulty_init():
        """initialize dictionary for plain code editing"""
        diff_dict = {
            "easy": [10, 10, 10],
            "medium": [15, 15, 30],
            "hard": [20, 20, 80],
        }
        return diff_dict

    def redraw(self):
        """draws window again

        uses after player has pressed on the cross in game"""
        self.window.build()
        self.window.clear()
        self.start_button.draw(self.img_dict["start"])
        self.difficulty_button.draw(self.img_dict[self.difficulty])
        self.exit_button.draw(self.img_dict["exit"])

    def update(self, event_list):
        """process events, menu logic included"""
        for event in event_list:
            if event.type == pygame.QUIT:  # processing pressing on the cross
                sys.exit()
            elif pygame.mouse.get_pressed()[0] and (event.type == pygame.MOUSEBUTTONDOWN): # processing menu logic on click
                if self.start_button.check_click():  # processing click on start button
                    self.minesweeper = Minesweeper(self.diff_dict[self.difficulty][0],\
                                    self.diff_dict[self.difficulty][1], self.diff_dict[self.difficulty][2])
                    self.minesweeper.play()
                    self.redraw()
                if self.difficulty_button.check_click():  # processing click on difficulty button
                    keys = list(self.diff_dict.keys())
                    self.difficulty = keys[(keys.index(self.difficulty) + 1) % 3]
                    self.difficulty_button.draw(self.img_dict[self.difficulty])
                if self.exit_button.check_click():  # processing click on exit button
                    sys.exit()
                pygame.display.flip()

    def start(self):
        """Main cycled function that generates events."""
        while 1:
            event_list = pygame.event.get()
            if event_list:
                self.update(event_list)


if __name__ == '__main__':
    menu = Menu()
    menu.start()
