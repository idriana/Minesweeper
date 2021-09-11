Minesweeper class
=================

Game class.

Main game class, that constains minesweeper's code.

Input values
^^^^^^^^^^^^

    sizex : int - number of cells in line

    sizey : int - number of cells in column

    count : int - amount of mines, that will be at field.

Fields
^^^^^^

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

    free_cells: matrix - True if there is no mine, False otherwise.

img_init()
^^^^^^^^^^

Load images for the game. ::

    def img_init() -> List[Surface]

Static method for creating list of images for the game.

update()
^^^^^^^^

Process events. ::

    def update(self, event_list : Eventlist) -> None

Sort and process every event in event_list.

game_logic()
^^^^^^^^^^^^

Process game logic. ::

    def game_logic(self, x : int = -1, y : int = -1) -> None

There is only mause control, so it processes only mouse events.

play()
^^^^^^

Main cycled function that generates events. ::

    def play(self) -> None

Generate events while the game is not closed. When user close game window, program goes back to menu.

