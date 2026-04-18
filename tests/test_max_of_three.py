from unittest import TestCase, main
from exercises.max_of_three import verificar_maior

class TestMaxOfThree(TestCase):

    def test_positive_numbers(self):
        actual = verificar_maior(10, 5, 1)
        expected = 10
        self.assertEqual(expected, actual)

    def test_negative_numbers(self):
        actual = verificar_maior(-1, -5, -4)
        expected = -1
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    main()
