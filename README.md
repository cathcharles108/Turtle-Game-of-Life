# Turtle-Game-of-Life
Implementations of Conway's Game of Life using Python's Turtle package. The first version is fully automated where the program randomizes the initial configuration and plays the game based on that. The second version is interactive and allows the user to set the initial configuration, and, during the game itself, also change the speed of the game.

# What is the Game of Life?
From Wikipedia.com: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves."

Find also the rules of the Game on Wikipedia: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

# Version 1 Details
This version is fully automated, where the computer sets the initial configuration and all the user does is observe the results as they evolve. Some details of the game implementation:
- The screen is a 50x50 grid
- A cell that is filled with color is 'alive'
- When initializing, the program assigns a 1/5 chance of any cell becoming alive
- The color of a cell is randomized from a selection of pastel colors at every iteration
- The program wraps around the edges of the board (i.e. the row above the first row is the last row)
- The program counts how many cells are alive and tracks how much time has passed since the start

# Version 2 Details
This version is an expansion of version 1. Instead of the program assigning the initial configuration, the user simply clicks on a cell in the start grid to activate it, and click on it again to deactivate it. The user then begins the gameplay by pressing the spacebar. From there, most of the gameplay is the same as the previous version, with a couple of differences:
- The cells of the grid are not visible in the first version. They are made visible in this one so that they are easier to click on.
- Version 2 allows the user to change the speed of how fast the game evolves on a scale of 1-9. In version 1, the speed is defaulted to setting 7.

# Next Steps
These two implementations of the Game of Life still have many limitations. In future versions, I plan to (at the very least) add a reset button, as well as expand the limits of the game a little further.
