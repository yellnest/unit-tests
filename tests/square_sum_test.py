from unittest import TestCase, main

from main import square_sum


class SquareSumTest(TestCase):
    def test_square_sum(self):
        self.assertEqual(square_sum([0, 3, 4, 5]), 50)

    def test_negative_sum(self):
        with self.assertRaises(ValueError) as e:
            square_sum([-1, 3, 4, 5])
        self.assertEqual('Число должно быть положительным', e.exception.args[0])


if __name__ == '__main__':
    main()
