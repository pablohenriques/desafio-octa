from unittest import TestCase
from exercises.vectors import search, insert, remove

class TestSearchVector(TestCase):

    def test_search_nothing_list(self):
        actual: int = search([], 1)
        expected: int = -1
        self.assertEqual(expected, actual)

    def test_search_list(self):
        actual: int = search([1, 2, 3], 1)
        expected: int = 0
        self.assertEqual(expected, actual)

    def test_search_not_found(self):
        actual: int = search([1, 2, 3], 5)
        expected: int = -1
        self.assertEqual(expected, actual)

    def test_search_last_element(self):
        actual: int = search([1, 2, 3], 3)
        expected: int = 2
        self.assertEqual(expected, actual)

    def test_raise_error_len_list(self):
        with self.assertRaises(ValueError):
            insert([], 1, 1)

    def test_raise_error_index(self):
        with self.assertRaises(ValueError):
            insert([1], 1, -1)

    def test_insert_list(self):
        actual: list = insert([1, 2, 3], 5, 0)
        expected: list[int] = [5, 1, 2, 3]
        self.assertEqual(expected, actual)

    def test_insert_0_list(self):
        actual: list = insert([1, 2, 3], 0, 4)
        expected: list[int] = [1, 2, 3, 0, 0]
        self.assertEqual(expected, actual)

    def test_insert_extends_with_value(self):
        actual: list = insert([1, 2, 3], 10, 5)
        expected: list[int] = [1, 2, 3, 0, 0, 10]
        self.assertEqual(expected, actual)

    def test_remove_not_found(self):
        actual: int = remove([1, 2, 3], 5)
        expected: int = -1
        self.assertEqual(expected, actual)

    def test_remove_modifies_list(self):
        v = [1, 2, 3]
        remove(v, 2)
        self.assertEqual([1, 3], v)

    def test_remove_returns_index(self):
        actual: int = remove([1, 2, 3], 2)
        expected: int = 1
        self.assertEqual(expected, actual)

    def test_remove_first_occurrence(self):
        v = [1, 2, 2, 3]
        remove(v, 2)
        self.assertEqual([1, 2, 3], v)
