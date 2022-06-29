import sys
from typing import Iterator, Any, Iterable, Optional

from node import Node


class LinkedList:
    def __init__(self, node: Iterable = None):
        self.len = 0
        self.head: Optional[Node] = None
        self.tail = self.head

        if node is not None:
            for value in node:
                self.append(value)

    def append(self, value: Any):
        append_node = Node(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1

    def step_by_step_on_nodes(self, index: int) -> Node:
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:

            left_node.next = right_node

    def __getitem__(self, index: int) -> Any:
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index: int):
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        if index == 0:
            self.head = self.head.next
        elif index == self.len - 1:
            tail = self.step_by_step_on_nodes(index - 1)
            tail.next = None
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            del_node = prev_node.next
            next_node = del_node.next

            self.linked_nodes(prev_node, next_node)

        self.len -= 1

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"

    def nodes_iterator(self) -> Iterator[Node]:
        current_node = self.head
        for _ in range(self.len):
            yield current_node
            current_node = current_node.next

class DoubleLinkedList(LinkedList):
    class Node:
        prev = None
        next_ = None
        value = None

        def __init__(self, value=None, next_=None, prev=None):
            self.value = value
            self.next_ = next_
            self.prev = prev

    head = None
    tail = None
    len_ = None

    def add(self, value):
        self.len += 1
        if not self.head:
            self.head = self.Node(value)
            return value
        elif not self.tail:
            self.tail = self.Node(value, None, self.head)
            self.head.next_ = self.tail
            return value
        else:
            self.tail = self.Node(value, None, self.tail)
            self.tail.prev.next_ = self.tail
            return value

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next_


if __name__ == '__main__':
    dl = DoubleLinkedList()
    dl.add(5)
    dl.add(2)
    dl.add(1)
    dl.add(4)
    dl.add(10)
    for value in dl:
        print(value)

    ll = LinkedList([1, 2, 3, 4, 5])

    print(sys.getrefcount(ll.head))

    for node in ll.nodes_iterator():
        print(sys.getrefcount(node))
