from unittest import TestCase
from exercises.leap_year import leap_year

class TestLeapYear(TestCase):

    def test_year_2000(self):
        actual = leap_year(2000)
        expected = True
        self.assertEqual(expected, actual)

    def test_year_1900(self):
        actual = leap_year(1900)
        expected = False
        self.assertEqual(expected, actual)

    def test_year_2024(self):
        actual = leap_year(2024)
        expected = True
        self.assertEqual(expected, actual)

    def test_year_2023(self):
        actual = leap_year(2023)
        expected = False
        self.assertEqual(expected, actual)

