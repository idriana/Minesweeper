Button class
============

Menu button class

Input values:
^^^^^^^^^^^^^

    id : int - number of button in the menu.

    amount : int - amount of buttons in the menu.

    rect : Rect - rectangle object from PyGame lib.

    window : Window - Window class object from Minesweeper module.

Fields:
^^^^^^^

    id : int - number of the button in menu

    screen : Surface - screen, on which counter will be drawed

    rect : Rectangle - Rectangle object from pygame. Rectangle object for button displaying

check_click() 
^^^^^^^^^^^^^

Check if button has been pressed. ::

    def check_click(self, x : int = -1, y : int = -1) -> bool

Can get x, y, simulating clicking.
If x and y are undefined, reads mouse pos.

draw()
^^^^^^
        
Draw button image. ::

    def draw(self, image : Surface) -> None

Gets displaing image as param.


