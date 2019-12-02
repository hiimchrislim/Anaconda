"""
The Anaconda: A Game

=== Module Description ===

This module holds the snake player and manages its movement along with how
it will grow.
"""

import pygame
from typing import Tuple

import linked_list

BODY_HEAD = pygame.Rect((132, 363, 32, 32))
BODY_PART = pygame.Rect((100, 363, 32, 32))


class Snake:
    def __init__(self):
        # Load in snake head sprite
        # Load in snake tail sprites

        self.snake_body = linked_list.LinkedList([BODY_HEAD])
        self.dx = 2  # snake moves as soon as game starts
        self.dy = 0

    def move_snake(self, event):
        # TODO: Implement
        pass

    def get_snake_direction(self) -> Tuple[int, int]:
        return self.dx, self.dy

    def grow(self) -> None:
        """
        Grows the body of the snake whenever food is encountered
        """
        self.snake_body.insert(len(self.snake_body), BODY_PART)
