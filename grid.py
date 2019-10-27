"""
Grid

=== Module Description ===
This module contains the implementation and the Grid
"""
from typing import List, Optional, Any
from linked_list import _Node


class Grid:
    """
    === Public Attributes ===
    _grid:
        The grid of the game being represented by a 2D array
    """
    _grid = []

    def __init__(self, size: int):
        """Initialize the Grid with the given size"""
        self.size = size
        self._make_grid

    def get_size(self) -> int:
        """
        :return: The size of the grid
        """
        return self.size

    def _make_grid(self) -> None:
        """
        Makes the gameboard grid of the game
        """
        for _ in self.size:
            col = []
            for _ in self.size:
                col.append(None)
            self._grid.append(col.copy())

    def insert(self, item: Any, col: int, row: int) -> None:
        """Inserts an item into the specific column and row of the grid"""
        self._grid[row][col] = item

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
        return self.grid[x][y]
