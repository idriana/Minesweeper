Menu class
==========

Menu class.

In menu player can click on 3 buttons:

    Start button - to start the game;

    Difficulty button (easy/medium/hard) - to pick difficulty;

    Exit button - to close the app.

Input values:
^^^^^^^^^^^^^

None.

Fields
^^^^^^

    window : Window - window, in which application works

    screen : Surface - screen, on which counter will be drawed

    img_dict : List[Surface] - list with images for the game

    diff_dict : dict - difficulty dictionary for easier coding

    difficulty : str - current difficulty level

    start_button : Button - first button in menu, which starts the game

    difficulty_button : Button - second button in menu, which defines difficulty level of the game

    exit_button : Button - the last button in menu, which exits the game

    minesweeper : Minesweeper - game object

Image_init()
^^^^^^^^^^^^

Initialize pictures dictionary. ::

    def image_init(): -> List[Surface]

Static method for creating list of images for menu.

difficulty_init()
^^^^^^^^^^^^^^^^^

Initialize difficulty dictionary. ::

    def difficulty_init() -> dict

Static method for creating dictionary for plain difficulty coding.

redraw()
^^^^^^^^

Draw window. ::

    def redraw(self): -> None

Usually used after game has ended to return settings fitting for menu.

update():
^^^^^^^^^

Process events. ::

    def update(self, event_list : Eventlist) -> None

Sort and process every event in event_list. Also contains logic for buttons.

start()
^^^^^^^

Main cycled function that generates events. ::

        def start(self) -> None

After event_list generated, it goes to update() function.            