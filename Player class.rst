Player class
============

Class for player and flag buttons.

Manage game modes by 2 buttons.

Input values:
^^^^^^^^^^^^^

    window : Window - Window class object. Contains screen, on which buttons will be drawed

    img_dict : List[Surface] - list with images for the game

    space : int - range between window's and field's top

Fields
^^^^^^

    flagging : bool - Statement var, which defines, if the player puts the flag

    game : bool - Statement vat, which defines, if the game is over

    screen : Surface - screen, on which counter will be drawed

    img_dict : List[Surface] - list with images for the game

    player_rect : Rectangle - Rectangle object from pygame. Rectangle object for player button displaying

    flag_rect : Rectangle - Rectangle object from pygame. Rectangle object for flag button displaying

player_draw()
^^^^^^^^^^^^^

Draw player button. ::

    def player_draw(self, passed : bool = False) -> None

Draw button image depending on whether the game continues.

flag_draw()
^^^^^^^^^^^

Draw flag button. ::

    def flag_draw(self) -> None

Draw button image depending on whether the flags are setting.

flag_click()
^^^^^^^^^^^^

Process click on the flag button. ::

    def flag_click(self) -> None

Reverse flagging (game mode) param.
Also call flag_draw() function.

player_click()
^^^^^^^^^^^^^^

Process click on the player button. ::

    def player_click(self) -> None

Set game param to True, that means game is not over. Also draw player button image.
