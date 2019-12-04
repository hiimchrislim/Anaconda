"""The Anaconda: A Game
=== Module Description ===
This module holds the snake player and manages its movement along with how
it will grow.
"""
import pygame
from typing import Tuple
# BODY_HEAD = pygame.Rect((132, 363, 32, 32))
# BODY_PART = pygame.Rect((100, 363, 32, 32))


class Snake:
    def __init__(self, snake_linked_list, dx=1, dy=0):
        self.snake_linked_list = snake_linked_list
        self.dx = dx  # snake moves right as soon as game starts
        self.dy = dy

        # Load in snake head sprite
        # Load in snake tail sprites
        # self.snake_body = linked_list.LinkedList([BODY_HEAD])

    def get_snake_linked_list(self):
        return self.snake_linked_list

    def move_snake(self, event) -> None:
        """Changes the direction of the snake by updating dx and dy.
        Cannot reverse 180 degrees.
        """
        x, y = self.get_snake_direction()
        if event.key == pygame.K_w and x != 0 and y != 1:  # (dy < 0) = Moves up the canvas (index decreases)
            self.dx, self.dy = 0, -1
        elif event.key == pygame.K_a and x != 1 and y != 0:  # (dx < 0) = Moves left (index decreases)
            self.dx, self.dy = -1, 0
        elif event.key == pygame.K_s and x != 0 and y != -1:  # (dy > 0) = Moves down the canvas (index increases)
            self.dx, self.dy = 0, 1
        elif event.key == pygame.K_d and x != -1 and y != 0:  # (dx > 0) = Moves right (index increases)
            self.dx, self.dy = 1, 0
        else:
            pass

    def update(self):
        curr = self.snake_linked_list._first
        previous_coordinate = curr.item
        new_coord_x = previous_coordinate[0] + self.dy
        new_coord_y = previous_coordinate[1] + self.dx
        new_coord = (new_coord_x, new_coord_y)
        curr.insert_item(new_coord)
        curr = curr.next
        while curr is not None:
            old_coord = curr.item
            curr.insert_item(previous_coordinate)
            previous_coordinate = old_coord
            curr = curr.next

    def get_snake_direction(self) -> Tuple[int, int]:
        return self.dx, self.dy

    def grow(self) -> None:
        """
        Grows the body of the snake whenever food is encountered
        """
        curr = self.snake_linked_list._first
        head_pos = curr.item
        direction = self.get_snake_direction()
        body = None
        if direction[0] == 1:
            body = (head_pos[0] + 1, head_pos[1])
        elif direction[0] == -1:
            body = (head_pos[0] - 1, head_pos[1])
        elif direction[1] == -1:
            body = (head_pos[0], head_pos[1] + 1)
        else:
            body = (head_pos[0], head_pos[1] - 1)
        self.snake_linked_list.insert(0, body)