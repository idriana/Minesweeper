Window class
============

Window class.

Contains functions that affects whole display.

Input values:
^^^^^^^^^^^^^

    width : int - window's width

    height : int - window's height

Fields
^^^^^^

    width : int - width of the window

    height : int - height of the window

    screen : Surface - Surface object from pygame, which is displayed every time

build()
^^^^^^^

Rebuild the field. ::

    def build(self): -> None

Use saved values width and height from class.

clear()
^^^^^^^

Clear the field. ::

    def clear(self) -> None

Fulfill screen with gray.