"""
The Anaconda: A Game

=== Module Description ===

This module holds the snake player and manages its movement along with how
it will grow.
"""

import pygame
from typing import Tuple


class Snake:
    def __init__(self):
        # Load in snake head sprite
        # Load in snake tail sprites

        self.dx = 2  # snake moves as soon as game starts
        self.dy = 0

    def move_snake(self, event):
        # TODO: Implement
        pass

    def get_snake_direction(self) -> Tuple[int, int]:
        return (self.dx, self.dy)
