#!/usr/bin/env python
"""Conway's Game of Life in Python

Authors:
    by u/mathnoob19

    Objectified by Phillyclause89

Sauces:
    https://www.reddit.com/r/learnpython/comments/e5ag24/looking_for_criticism_conways_game_of_life_in/

    https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

import random
import subprocess
import time


class GameOfLife:
    """
    GameOfLife
    Class for simulating the game of life by John Horton Conway

    Attributes:
        GameOfLife.markers (:obj:'dict'): Dictionary of game markers {0: dead_marker, 1: alive_marker} .

        GameOfLife.turn (:obj:`int`): Current turn the game instance is on.

        GameOfLife.max_turns (:obj:`int`): Maximum turns the game will play

        GameOfLife.grid (:obj:`list`): 2D list of integers (0=DEAD, 1=Alive) representing the game board

    """

    def __init__(self, max_turns=100, dead_marker="█", alive_marker="X"):
        """
        GameOfLife(self, max_turns=100, dead_marker="█", alive_marker="X")

        Initializes the GameOfLife class object to new game values

        Note:
            GameOfLife.turn and

        :param max_turns:    int    default: 100  (Maximum number of game turns to be played)

        :param dead_marker:  string default: "█" (Character(s) used for the dead squares when visualizing the board)

        :param alive_marker: string default: "X"  (Character(s) to be used for the living squares)

        """

        self.markers = {
            0: dead_marker,
            1: alive_marker}
        self.turn = 0
        self.max_turns = max_turns
        self.grid = self.generate_grid()

    @staticmethod
    def generate_grid():
        """
        @staticmethod

        GameOfLife.generate_grid():

        Creates the initial grid configuration during init method

        Note:
            Keep hard coded: population=[1, 0]

        :return: :obj:`list` of :obj:`int`:

        Todo:
            * Could turn weights and k and max range() values to attributes inited by __init__() params

        """

        return [random.choices(population=[1, 0], weights=[0.1, 0.9], k=50) for y in range(0, 50)]

    def cell_update(self):
        """
        GameOfLife.cell_update():

        Updates the grid for each time step.

        Rules for updating the grid:

           1. Any live cell with two or three neighbors survives.
           2. Any dead cell with three live neighbors becomes a live cell.
           3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.

        :return: <class 'NoneType'>

        """

        bounds_y = len(self.grid[0])
        bounds_x = len(self.grid)

        # Iterate over each cell
        for x in range(0, len(self.grid)):
            for y in range(0, len(self.grid[0])):
                # For each cell, calculate the number of its live neighbors:
                neighbors = sum((
                    self.grid[x][(y + 1) % bounds_y],
                    self.grid[x][(y - 1) % bounds_y],
                    self.grid[(x + 1) % bounds_x][y],
                    self.grid[(x - 1) % bounds_x][y],
                    self.grid[(x + 1) % bounds_x][(y + 1) % bounds_y],
                    self.grid[(x + 1) % bounds_x][(y - 1) % bounds_y],
                    self.grid[(x - 1) % bounds_x][(y + 1) % bounds_y],
                    self.grid[(x - 1) % bounds_x][(y - 1) % bounds_y]))
                # If the cell is alive and has 2-3 neighbors then leave it alone
                # If the cell is dead and has three neighbors then it becomes alive
                if not (neighbors == 2 or neighbors == 3):
                    self.grid[x][y] = 0
                elif neighbors == 3 and self.grid[x][y] == 0:
                    self.grid[x][y] = 1

    def convert_to_string(self, x):
        """
        GameOfLife.convert_to_string(self, x):

        :param x: value to compare;

        :return: str (marker to be used for visualizing square on board

        """

        return self.markers[0] if x == 0 else self.markers[1]

    def grid_display(self):
        """
        GameOfLife.grid_display():

        Formats and displays the grid!

        """

        display = ''
        for x in range(0, len(self.grid)):
            display += f"{''.join(list(map(self.convert_to_string, self.grid[x])))}\n"
        print(display)

    def play(self, pause=0.5, show=True):
        """
        GameOfLife.play(self, show=True, pause=0.5)

        :param pause: int or float (how long to show the board)

        :param show: boolean (Print board to console)

        :return: <class 'NoneType'>

        """

        while self.turn < self.max_turns:
            if show:
                subprocess.call('cls||clear', shell=True)
                self.grid_display()
                time.sleep(pause)
            self.cell_update()
            self.turn += 1
        self.reset_game()

    def reset_game(self, new_max_turns=None):
        """
        reset_game(self, new_max_turns=None)

        :param new_max_turns: None or int use to set new max turns

        :return: <class 'NoneType'>

        """

        self.turn = 0
        self.grid = self.generate_grid()
        if new_max_turns:
            self.max_turns = new_max_turns


if __name__ == "__main__":
    game = GameOfLife(420, "\033[1;m|  |", "|\033[1;35m:P\033[1;m|")
    game.play()

    # Code from a Debug Tool I use when I write code
    # Available https://github.com/Phillyclause89/SPyObject
    """ 
    from spyobject import SPyObject as SPy
    game = GameOfLife()
    SPy(game, globals()).obj_info()
    SPy(game.play(), globals()).obj_info()
    SPy(game.cell_update(), globals()).obj_info()
    SPy(game.generate_grid(), globals()).obj_info()
    SPy(game.convert_to_string(1), globals()).obj_info()
    SPy(game.convert_to_string(0), globals()).obj_info()
    SPy(game.grid_display(), globals()).obj_info()
    """
