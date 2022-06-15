from typing import Any, Optional
class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = next_
    def __repr__(self):
        return f"Node({self.value}, {self.next})"

    def __str__(self):
        return f"({self.value}, {self.next})"

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError


class DoubleLinkedNode(Node):
    ...


if __name__ == "__main__":
    node1 = Node(4)
    print(node1)

def test__node__str__():
    node = Node()
    expected = 5
    actual =str(node)
    assert expected == actual
