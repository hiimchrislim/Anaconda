""" The Anaconda: A Game

=== Module Description ===
This module contains the implementation of the Anaconda Game.
"""

from __future__ import annotations
from grid import Grid
from typing import Any, List, Optional, Tuple
from linked_list import LinkedList, _Node
import pygame


class Anaconda:
    """
    Implementation of the Anaconda Game.
    """

    # === Private Attributes ===
    # _snake: A LinkedList representation of the snake
    # _grid: The grid of game
    _snake = None
    _grid = None

    def __init__(self) -> None:
        """Initialize a new Anaconda Game.
        """
        raise NotImplementedError

    def make_grid(self) -> None:
        """
        Makes a 16X16 Grid (model).
        """
        self._grid = Grid(16)

    def make_food(self) -> None:
        """
        Makes food to eat for the Anaconda.
        """
        raise NotImplementedError

    def make_snake(self) -> None:
        """
        Makes the body of the Anaconda.
        """
        initial_snake_body = []
        for col in range(4):
            initial_snake_body.append(_Node((8, col)))
        self._snake = LinkedList(initial_snake_body)

    def get_snake(self) -> LinkedList:
        """
        Returns the snake in the form of a LinkedList
        """
        return self._snake

    def stage_gui(self) -> None:
        """
        Display an interactive graphical display of the game.
        """
        raise NotImplementedError

    def movement(self) -> None:
        """
        Determines the direction in which the Anaconda should move.
        """
        raise NotImplementedError

    def place_food(self) -> None:
        """
        Places the food randomly for the snake to it.
        """
        raise NotImplementedError

    def game_over(self) -> None:
        """
        Determines whether or not the game is over.
        """
        raise NotImplementedError

    def grow(self) -> None:
        """
        Grows the body of the snake by 1 unit when food is eaten.
        """
        raise NotImplementedError

    def display_stats(self) -> None:
        """
        Displays the score of the player.
        """
        raise NotImplementedError

    def restart_game(self) -> None:
        """
        Restart the game when the game is over.
        """
        raise NotImplementedError
