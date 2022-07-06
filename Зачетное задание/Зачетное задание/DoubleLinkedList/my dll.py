class Dbllist:
    class Node:
        previous_node = None
        next_node = None
        element = None

        def __init__(self, element, next_node=None, previous_node=None) -> None:
            self.element = element
            self.next_node = next_node
            self.previous_node = previous_node


        def __repr__(self):
            next_prev = None if self.previous_node is None else f"DoubleLinkedNode({self.prev})"
            next_repr = None if self.next is None else f"DoubleLinkedNode({self.next})"
            return f"DoubleLinkedNode({self.value}, {next_prev}, {next_repr})"

        def __str__(self) -> str:
            return str(self.value)
    head = None
    tail = None
    length = 0
    def add(self, element):
        """Добовление элементов"""
        self.length += 1
        if not self.head:
            self.head = self.Node(element)
            return element
        elif not self.tail:
            self.tail = self.Node(element, None, self.head)
            self.head.next_node = self.tail
        else:
            self.tail = self.Node(element, None, self.tail)
            self.tail.previous_node.next_node = self.tail
            return element
    def __iter__(self):
        """Назначаем голову"""
        node = self.head

        while node:
            yield node.element
            node = node.next_node
if __name__ == '__main__':
    dbllist = Dbllist()
    dbllist.add(3)
    dbllist.add(14)
    dbllist.add(24)
    dbllist.add(145)
    dbllist.add(5)

    for e in dbllist:
        print(e)