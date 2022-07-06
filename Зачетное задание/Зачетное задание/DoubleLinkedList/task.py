import sys
from typing import Iterator, Any, Iterable, Optional

from node import DoubleLinkedNode, Node


class LinkedList:
    def __init__(self, data: Iterable = None):
        self.len = 0
        self.head: Optional[Node] = None
        self.tail = self.head

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

    def insert(self, index: int):
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
        node = self.insert(index)
        return node

    def __setitem__(self, index: int, value: Any) -> None:
        node = self.insert(index)
        node.value = value
        return node.value

    def __delitem__(self, index: int):
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        if index == 0:
            self.head = self.head.next
        elif index == self.len - 1:
            tail = self.insert(index - 1)
            tail.next = None
        else:
            prev_node = self.insert(index - 1)
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


class DoubleLinkedList(LinkedList):

    @staticmethod
    def linked_nodes(left_node: DoubleLinkedNode, right_node: Optional[DoubleLinkedNode] = None) -> None:
        left_node.next = right_node
        right_node.prev = left_node

    def insert_in_emptylist(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Список не пустой")

        self.len += 1

    def insert_at_start(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            print("узел вставлен")
            return
        new_node = Node(data)
        new_node.tail = self.head
        self.head.prev = new_node
        self.head= new_node

    def __delitem__(self, index: int):
        super().__delitem__(index)

        self.len -= 1



if __name__ == '__main__':

    ll = LinkedList([1, 2, 3])

    print(sys.getrefcount(ll.head))

    for node in ll.nodes_iterator():
        print(sys.getrefcount(node))
    ll.append(4)

    dl = DoubleLinkedList([])
    dl.insert_in_emptylist(2)
    print(dl)
    dl.insert_at_start(8)
    print(dl)

    # dl.__delitem__(0)


    for value in dl:
        print(value)
