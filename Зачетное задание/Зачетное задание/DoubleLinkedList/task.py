import sys
from typing import Iterator, Any, Iterable, Optional

from node import Node


class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        cur_node = self.head
        while


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

    # ll = LinkedList([1, 2, 3, 4, 5])
    #
    # print(sys.getrefcount(ll.head))
    #
    # for node in ll.nodes_iterator():
    #     print(sys.getrefcount(node))
