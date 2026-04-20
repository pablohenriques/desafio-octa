from unittest import TestCase
from exercises.armstrong import armstrong, armstrong_until

class TestArmstrong(TestCase):

    def test_armstrong_153(self):
        actual: int =  armstrong(153)
        expected: bool = True
        self.assertEqual(expected, actual)

    def test_armstrong_13(self):
        actual: int = armstrong(13)
        expected: bool = False
        self.assertEqual(expected, actual)

    def test_armstrong_9474(self):
        actual: int = armstrong(9474)
        expected: bool = True
        self.assertEqual(expected, actual)

    def test_armstrong_until_500(self):
        actual = armstrong_until(500)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]
        self.assertEqual(expected, actual)