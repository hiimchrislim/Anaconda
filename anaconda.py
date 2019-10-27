""" The Anaconda: A Game

=== Module Description ===
This module contains the implementation of the Anaconda Game.
"""

from __future__ import annotations
from typing import Any, List, Optional, Tuple
import linked_list
import pygame


class Anaconda:
    """
    Implementation of the Anaconda Game.
    """

    def __init__(self) -> None:
        """Initialize a new Anaconda Game.
        """
        raise NotImplementedError

    def make_grid(self) -> None:
        """
        Makes a 16X16 Grid on Pygame.
        """
        raise NotImplementedError

    def make_food(self) -> None:
        """
        Makes food to eat for the Anaconda.
        """
        raise NotImplementedError

    def make_snake(self) -> None:
        """
        Makes the body of the Anaconda.
        """
        raise NotImplementedError

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




