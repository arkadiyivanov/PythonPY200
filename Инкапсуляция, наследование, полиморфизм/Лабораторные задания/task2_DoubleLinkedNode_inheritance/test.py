from task import DoubleLinkedNode


def test_repr_doubl_linked_node():


    node = DoubleLinkedNode
    expected_value = "DoubleLinkedNode(5, None, None"
    actual_value = repr(node)
    assert expected_value == actual_value

def test_repr_doubl_linked_node_without_prev():
    next_node = DoubleLinkedNode(3)
    current_node = DoubleLinkedNode(2)

    current_node.next = next_node
    next_node.prev = current_node

    expected_value = "DoubleLinkedNode(2, DoubleLinkedNode(3, None, None), None)"

    actual_value = repr(current_node)

    assert expected_value == actual_value


if __name__ == "__main__":
    test_repr_doubl_linked_node()
    test_repr_doubl_linked_node_without_prev()