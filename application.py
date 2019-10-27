"""
The Anaconda: A Game

=== Module Description ===
This module is responsible for displaying the UI of the game and running the
overall anaconda game.
"""

from __future__ import annotations
from typing import Tuple
import pygame


class Application:
    """
    === Attributes ===
    Sprites: snakeH_sprite, snakeT_sprite, food_sprite
    window_size:
        size of the GUI window
    food_size:
        size of the food the snake eats
    snakeH_size:
        size of the snake's head
    snakeT_size:
        size of the snake's tail
    clock:
        manage how fast the screen refreshes (FPS)
    """
    window_size: Tuple[int, int]
    food_size: Tuple[int, int]
    snakeH_size: Tuple[int, int]
    snakeT_size: Tuple[int, int]
    clock: int

    def __init__(self) -> None:
        """
        Initialize the pygame module along with the window size and clock.
        Load in all the sprites.
        """
        pygame.init()
        self.window_size = (640, 480)
        self.clock = pygame.time.Clock()
        # TODO: Implement this method

    def show_title_screen(self) -> None:
        """
        Display the title screen of the game. The title screen should show the
        name of the game and its rules.
        """
        # TODO: Implement this method

    def display_score(self):
        """
        When the game is over, show the final score of the player.
        """
        # TODO: Implement this method

    def play(self) -> None:
        """
        Main GUI Application Loop. Runs the game.
        """
        # TODO: Implement this method
