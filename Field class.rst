MinesweeperField class
======================

class of the game field.

Input values:
^^^^^^^^^^^^^

    screen : Surface - screen, on which counter will be drawed

    sizex : int - number of cells in line

    sizey : int - number of cells in column

    count : int - amount of mines, that will be at field.

    width : int - window's width for correct image

    img_dict : List[Surface] - list with images for the game

Fields
^^^^^^

    screen : Surface - screen, on which timer will be drawed

    img_dict : List[Surface] - list with images for the game

    rect : Rectangle - Rectangle object from pygame for displaying images

    right : int - range between timer's right border and window's right border

    start : float - computer time in seconds when the game started

    event : EventType - EventType object from pygame. Needs to create new Events

gen()
^^^^^

Generate level. ::

    def gen(self) -> None

fill_cells()
^^^^^^^^^^^^

Generate statuses for every cell. ::

    def fill_cells(self) -> None

Makes four matrix:

    self.mined_cells : matrix - True if there is mine, False otherwise.

    self.checked_cells : matrix - True if cell is checked, False otherwise.

    self.flagged_cells: matrix - True if there is flag, False otherwise.

    self.free_cells: matrix - True if there is no mine, False otherwise.

inner_building()
^^^^^^^^^^^^^^^^

Draw closed cells for current size. ::

    def inner_building(self) -> None

border_building()
^^^^^^^^^^^^^^^^^

Draw borders for current size. ::

    def border_building(self) -> None

open_cell()
^^^^^^^^^^^

Open cell. ::

    def open_cell(self, x : int, y : int) -> bool

Gets column and line of cell to open. 
Return False if there was mine at the cell, True otherwise.

flag_cell()
^^^^^^^^^^^

Set flag status. ::

    def flag_cell(self, x : int, y : int) -> None

Gets column and line of cell to flag. 
Sets True if it was False and False if it was True.
All cells are False from the start.

draw_cell()
^^^^^^^^^^^

Draw cell depending on it's status. ::

    def draw_cell(self, x : int, y : int) -> None

Gets column and line of cell to draw. 

draw_mines()
^^^^^^^^^^^^

Draw every mine of the field. ::

    def draw_mines(self) -> None

Draw mines if cells are not opened and not flagged.