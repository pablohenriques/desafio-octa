from unittest import TestCase, main
from exercises.max_of_three import max_of_three

class TestMaxOfThree(TestCase):

    def test_positive_numbers(self):
        actual = max_of_three([10, 5, 1])
        expected = 10
        self.assertEqual(expected, actual)

    def test_negative_numbers(self):
        actual = max_of_three([-1, -5, -4])
        expected = -1
        self.assertEqual(expected, actual)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            max_of_three([])

if __name__ == "__main__":
    main()
