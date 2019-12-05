"""Grid
=== Module Description ===
This module contains the implementation and the Grid
"""
from typing import List, Optional, Any
from linked_list import _Node, LinkedList
from snake import Snake


class Grid:
    """
    === Public Attributes ===
    _grid:
        The grid of the game being represented by a 2D array
    """
    _grid = []
    snake = None

    def __init__(self, size: int):
        """Initialize the Grid with the given size"""
        self.size = size
        self._make_grid(self.size)
        self.game_over = False

    def get_size(self) -> int:
        """Return the size of the grid"""
        return self.size

    def _make_grid(self, size) -> None:
        """Makes the gameboard grid of the game"""
        for _ in range(size):
            col = []
            for _ in range(size):
                col.append(None)
            self._grid.append(col.copy())

    def insert(self, item: Any, row: int, col: int) -> None:
        """Inserts an item into the specific column and row of the grid"""
        try:
            self._grid[row][col] = item
        except IndexError:
            self.game_over = True

    def is_game_over(self):
        return self.game_over

    def get_grid(self) -> List[List]:
        """
        :return: The grid of the game
        """
        return self._grid

    def get_item(self, x: int, y: int) -> Optional[_Node]:
        """
        :param x: The x coordinate of the grid
        :param y: The y coordinate of the grid
        :return: The Node on the grid (if applicable), otherwise None
        """
        return self._grid[x][y]

    def draw_original_snake(self):
        initial_snake_body = []
        head = (10, 4)
        self.insert(head, 10, 4)
        initial_snake_body.append(head)
        for col in range(3, 0, -1):
            body = (10, col)
            self.insert(body, 10, col)
            initial_snake_body.append(body)
        self.snake = Snake(LinkedList(initial_snake_body))

    def _make_fresh_grid(self, size) -> None:
        """Makes the gameboard grid of the game"""
        lst = []
        for _ in range(size):
            col = []
            for _ in range(size):
                col.append(None)
            lst.append(col.copy())
        return lst

    def clear_grid(self) -> None:
        self._grid = self._make_fresh_grid(16)

    def draw_new_snake(self):
        (dx, dy) = self.snake.get_snake_direction()
        self.snake = Snake(self.snake.get_snake_linked_list(), dx, dy)
        curr = self.snake.get_snake_linked_list()._first
        while curr is not None:
            coord_x = curr.item[0]
            coord_y = curr.item[1]
            self.insert(curr, coord_x, coord_y)
            curr = curr.next

    def update_snake(self):
        self.snake.update()
        self.clear_grid()
        self.draw_new_snake()

    def move_snake(self, event):
        self.snake.move_snake(event)
