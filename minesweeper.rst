Minesweeper
===========

This is a core file, where application code is saved.
There contains and creates Minesweeper class.
Whole program made with classes, so this is full documentation for Minesweeper.

Classes
^^^^^^^

.. toctree::
   :maxdepth: 2

   Window class
   Timer class
   Counter class
   Player class
   Field class
   Minesweeper class

Start
^^^^^

Game can be started without menu via ::

   if __name__ == '__main__':
       game = Minesweeper(10, 10, count=20)
       game.play()



