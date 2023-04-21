import unittest
from positional_list import PositionalList


def list_to_positional_list(L: list) -> PositionalList:
    """ Return a new positional list that converted from the given list. """
    new_positional = PositionalList()
    for ele in L:
        new_positional.add_last(ele)
    return new_positional


class TestCountNodes(unittest.TestCase):
    def test_list_convertion(self):
        L = [2, 4, 8, 16, 32, 64]
        positional = list_to_positional_list(L)
        for pos_ele in positional:
            # When iterate through positional list, elements are in the same order as L
            self.assertEqual(pos_ele, L.pop(0))


if __name__ == "__main__":
    unittest.main()
