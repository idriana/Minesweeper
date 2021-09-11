Timer class
===========

Timer class

Class for timer at right top corner of the game.

Input values:
^^^^^^^^^^^^^

    screen : Surface - screen, on which timer will be drawed

    img_dict : List[Surface] - list with images for the game

    start : float - computer time in seconds when the game started

    space : int - range between window's and field's top

    right : int - range between timer's right border and window's right border

Fields
^^^^^^

    screen : Surface - screen, on which timer will be drawed

    img_dict : List[Surface] - list with images for the game

    rect : Rectangle - Rectangle object from pygame for displaying images

    right : int - range between timer's right border and window's right border

    start : float - computer time in seconds when the game started

    event : EventType - EventType object from pygame. Needs to create new Event

draw()
^^^^^^

Draw the timer. ::

    def draw(self) -> None

Draw timer image. When value is over 999, 999 is dispayed. There is always 3 positions at the timer.

reset()
^^^^^^^

Reset the timer. ::

    def reset(self) -> None

Set timer's start point to current time, making passed time equal to zero. Also call draw() function.



