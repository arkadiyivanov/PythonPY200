from typing import Any


class Node:

    def __init__(self, value: Any, next_=None):

        self.value = value
        self.next = next_

    def __repr__(self):
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    @staticmethod
    def is_valid(node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.is_valid(value)
        self.__next = value


class DoubleLinkedNode(Node):

    def __init__(self, value: Any, prev=None):
        super().__init__(value)
        self.prev = prev

    def __repr__(self):
        next_prev = None if self.prev is None else f"DoubleLinkedNode({self.prev})"
        next_repr = None if self.next is None else f"DoubleLinkedNode({self.next})"
        return f"DoubleLinkedNode({self.value}, {next_prev}, {next_repr})"

    def __str__(self) -> str:
        return str(self.value)

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        print("Вызван setter")
        self.is_valid(value)
        self.__prev = value


if __name__ == "__main__":
    first_node = Node(1)
    second_node = Node(2)

    first_node.next = second_node

    print(repr(first_node), repr(first_node.next))
    a = Node(4)
    b = Node(6)
    a.next = b
    print(repr(a), repr(b))
