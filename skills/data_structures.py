"""Common data structure implementations."""

from __future__ import annotations

__all__ = ["Stack", "Queue", "LinkedList"]


class Stack:
    """A simple LIFO stack."""

    def __init__(self) -> None:
        self._items: list = []

    def push(self, item: object) -> None:
        self._items.append(item)

    def pop(self) -> object:
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> object:
        if self.is_empty():
            raise IndexError("peek at empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return f"Stack({self._items!r})"


class Queue:
    """A simple FIFO queue."""

    def __init__(self) -> None:
        self._items: list = []

    def enqueue(self, item: object) -> None:
        self._items.append(item)

    def dequeue(self) -> object:
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)

    def peek(self) -> object:
        if self.is_empty():
            raise IndexError("peek at empty queue")
        return self._items[0]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return f"Queue({self._items!r})"


class _Node:
    """Internal node for LinkedList."""

    def __init__(self, data: object, next_node: _Node | None = None) -> None:
        self.data = data
        self.next = next_node


class LinkedList:
    """A singly linked list."""

    def __init__(self) -> None:
        self._head: _Node | None = None
        self._size: int = 0

    def prepend(self, data: object) -> None:
        """Insert an element at the beginning."""
        self._head = _Node(data, self._head)
        self._size += 1

    def append(self, data: object) -> None:
        """Insert an element at the end."""
        new_node = _Node(data)
        if self._head is None:
            self._head = new_node
        else:
            current = self._head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1

    def remove(self, data: object) -> None:
        """Remove the first occurrence of *data*. Raises ValueError if not found."""
        prev, current = None, self._head
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self._head = current.next
                self._size -= 1
                return
            prev, current = current, current.next
        raise ValueError(f"{data!r} not found in list")

    def to_list(self) -> list:
        """Return the linked list contents as a Python list."""
        result, current = [], self._head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"LinkedList({self.to_list()!r})"
