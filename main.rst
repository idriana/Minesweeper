Main
====

This is the main file, from which application is supposed to start.
There contains menu class and creates game(Minesweeper) class.
Whole program made with classes, so this is full documentation for Main

Classes
^^^^^^^

.. toctree::
   :maxdepth: 2

   Button class
   Menu class

Start
^^^^^

Project starts via ::

    if __name__ == '__main__':
        menu = Menu()
        menu.start()


