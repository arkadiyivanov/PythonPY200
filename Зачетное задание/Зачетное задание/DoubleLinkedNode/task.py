from typing import Any, Optional

class Node:

    def __init__(self, value: Any, next_: Optional["Node"] = None):

        self.value = value
        self.next = next_

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        print("Вызван setter")
        self.is_valid(value)
        self.__next = value


class DoubleLinkedNode(Node):

    def __init__(self, value: Any, prev=None):
        super().__init__(value)
        self.prev = prev

    def __repr__(self) :
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
    f_node = Node(1)
    s_node = Node(2)


    f_node.next = s_node

    print(repr(f_node), repr(f_node.next))
