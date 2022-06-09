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

class DoubleLinkedNode(Node):
    ...


if __name__ == "__main__":
    ...

def test__node__str__():
    node = Node()
    expected = 5
    actual =str(node)
    assert expected == actual