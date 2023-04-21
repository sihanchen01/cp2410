import unittest
from circular_linked_list import CircularLinkedList


class TestCountNodes(unittest.TestCase):
    def test_initial_value(self):
        circular = CircularLinkedList()
        # expect initial value 0 -- empty linked list
        self.assertEqual(circular.count_nodes(), 0)

    def test_count(self):
        circular = CircularLinkedList()
        # insert 12 nodes, all nodes have value 1234
        for i in range(12):
            circular.push(1234)
        self.assertEqual(circular.count_nodes(), 12)

    def test_pop(self):
        circular = CircularLinkedList()
        circular.push(1234)
        self.assertEqual(circular.count_nodes(), 1)
        circular.pop()
        self.assertEqual(circular.count_nodes(), 0)


if __name__ == "__main__":
    unittest.main()
