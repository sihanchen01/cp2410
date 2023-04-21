import unittest
from positional_list import PositionalList


def list_to_positional_list(L: list) -> PositionalList:
    """ Return a new positional list that converted from the given list. """
    new_positional = PositionalList()
    for ele in L:
        new_positional.add_last(ele)
    return new_positional


class TestCountNodes(unittest.TestCase):
    def test_empty_list(self):
        positional = PositionalList()
        self.assertEqual(positional.find_max(), None)

    def test_find_max_element(self):
        L = [2, 4, 8, 16, 32, 64, 128, 0, -23]
        positional = list_to_positional_list(L)
        self.assertEqual(positional.find_max(), 128)


if __name__ == "__main__":
    unittest.main()
