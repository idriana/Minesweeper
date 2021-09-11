Counter class
=============

Counter class

Count amount of mines left to flag. 

Input values:
^^^^^^^^^^^^^

    screen : Surface - screen, on which counter will be drawed

    img_dict : List[Surface] - list with images for the game

    amount : int - initial amount of mines on the field

    space : int - range between window's and field's top

Fields
^^^^^^

    screen : Surface - screen, on which counter will be drawed

    img_dict : List[Surface] - list with images for the game

    rect : Rectangle - Rectangle object from pygame for displaying images

    amount : int - initial amount of mines on the field

    length : int - amount of timer poses to be displayed

draw()
^^^^^^

Draw counter. ::

    def draw(self) -> None

Display amount of mines left to flag. When this number is lower than zero, zero is displayed. Also there at least 3 positions at the counter.

add()
^^^^^

Add 1 to amount of mines left. ::

    def add(self) -> None

Also call draw() function.

substract()
^^^^^^^^^^^

Substract 1 from amount of mines left. ::

    def substracy(self) -> None

Also call draw() function.

reset()
^^^^^^^

Set counter to param value. ::

    def reset(self, amount : int) -> None

Also call draw() function.
