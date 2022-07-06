import sys
from abc import ABC
from typing import Iterator, Any, Iterable, Optional
from collections.abc import MutableSequence

from node import DoubleLinkedNode, Node


class LinkedList(MutableSequence):

    def __len__(self) -> int: # fixme реализовать метод
        if self.head is None:
            return 0
        else:
            return sum(1 for _ in self)



    def count(self, value: Any) -> int:

        ...

    def __init__(self, data: Iterable = None):
        self.len = 0
        self.head = None
        self.tail = None

        if data is not None:
            for element in data:
                self.append(element)



    def append(self, element: Any):
        append_node = Node(element)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1

    def step_by_step(self, index):  # fixme rename step_by_step
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    def is_valid(self, index):
        if not isinstance(index, int):  # todo сделать отдельный метод is_valid_index (DRY)
            raise TypeError()

        if not 0 <= index < self.len:
            raise IndexError()


    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        left_node.next = right_node

    def __getitem__(self, index: int):
        return self.step_by_step(index)

    def __setitem__(self, index: int, value: Any) -> None:
        node = self.step_by_step(index)
        node.value = value
        return node.value

    def __delitem__(self, index: int):
        if index == 0:
            self.head = self.head.next
        elif index == self.len - 1:
            tail = self.step_by_step(index - 1)
            tail.next = None
        else:
            prev_node = self.step_by_step(index - 1)
            del_node = prev_node.next
            next_node = del_node.next

            self.linked_nodes(prev_node, next_node)

        self.len -= 1

    def to_list(self):
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


class DoubleLinkedList(LinkedList, ABC):

    @staticmethod
    def linked_nodes(left_node: DoubleLinkedNode, right_node: Optional[DoubleLinkedNode] = None) -> None:
        left_node.next = right_node
        right_node.prev = left_node

    def append(self, element):
        append_node = DoubleLinkedNode(element)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1


    def __delitem__(self, index: int):
        super().__delitem__(index)

        self.len -= 1


if __name__ == '__main__':


    ll = LinkedList([1,2,3])

    print(sys.getrefcount(ll.head))

    for node in ll.nodes_iterator():
        print(sys.getrefcount(node))
    ll.append(4)
    ll.append(2)
    print(ll)


    dl = DoubleLinkedList()
    dl.append(3)
    dl.append(4)
    dl.append(6)
    dl.append(35)
    print(dl)


    # print(dl.__getitem__(2))
    # print(dl.__setitem__(2, 1))
    # print(dl.__delitem__(3))
    # print(dl)
    print()


    for value in dl:
        print(value)

