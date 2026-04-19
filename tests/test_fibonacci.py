from unittest import TestCase, skip
from exercises.fibonnaci import fibonnaci

class TestFibonacci(TestCase):

    def test_case_5(self):
        actual = fibonnaci(5)
        expected = "0; 1; 1; 2; 3"
        self.assertEqual(expected, actual)

    def test_case_7(self):
        actual = fibonnaci(7)
        expected = "0; 1; 1; 2; 3; 5; 8"
        self.assertEqual(expected, actual)

    def test_case_50(self):
        actual: str = fibonnaci(50)
        expected: int = len(actual.split(";"))
        self.assertEqual(expected, 50)
