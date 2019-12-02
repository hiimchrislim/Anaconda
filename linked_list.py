"""Linked List

=== Module Description ===
This module contains the implementation and Linked List and _Node
"""
from __future__ import annotations
from typing import Any, List, Optional


class _Node:
    """A node in a linked list.

    === Attributes ===
    item:
        The data in this node.
    next:
        The next node in the list or None
    """
    item: Any
    next: Optional[_Node]

    def __init__(self, item: Any) -> None:
        """Initialize a new node with <item>, with no next node.
        """
        self.item = item
        self.next = None  # Initially pointing to nothing


class LinkedList:
    """A linked list implementation of the List ADT.
    """
    # === Private Attributes ===
    # _first:
    #     The first node in the linked list, or None if the list is empty.
    _first: Optional[_Node]
    items: List

    def __init__(self, items: List) -> None:
        """Initialize a new empty linked list containing the given items.
        """
        if items == []:
            self._first = None
        else:
            self._first = _Node(items[0])
            if len(items) > 1:
                curr = self._first
                for i in items[1:len(items)]:
                    curr.next = _Node(i)
                    curr = curr.next

    def is_empty(self) -> bool:
        """Return whether the linked list is empty.

        >>> LinkedList([]).is_empty()
        True
        >>> LinkedList([1, 2, 3]).is_empty()
        False
        """
        return self._first is None

    def insert(self, index: int, item: Any) -> None:
        """Insert a the given item at the given index in this list.

        Raise IndexError if index > len(self) or index < 0.
        """
        # Create new node containing the item
        new_node = _Node(item)

        if index == 0:
            self._first, new_node.next = new_node, self._first
        else:
            # Iterate to (index-1)-th node.
            curr = self._first
            curr_index = 0
            while curr is not None and curr_index < index - 1:
                curr = curr.next
                curr_index += 1

            if curr is None:
                raise IndexError
            else:
                # Update to insert new node
                curr.next, new_node.next = new_node, curr.next

    def __getitem__(self, index: int) -> Any:
        """Return the item at position index in this list.

        Raise IndexError if index is >= the length of this list.
        """
        curr = self._first
        curr_index = 0

        while curr is not None and curr_index < index:
            curr = curr.next
            curr_index += 1

        if curr is None:
            raise IndexError
        else:
            return curr.item

    def __len__(self) -> int:
        """Return the number of elements in this list.
        """
        curr = self._first
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next
        return count
