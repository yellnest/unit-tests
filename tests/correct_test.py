from unittest import TestCase, main

from main import correct_symbol


class CorrectTest(TestCase):
    def test_5(self):
        self.assertEqual(correct_symbol('PARI5'), 'PARIS')

    def test_1(self):
        self.assertEqual(correct_symbol('DUBL1N'), 'DUBLIN')

    def test_0(self):
        self.assertEqual(correct_symbol('L0ND0N'), 'LONDON')


if __name__ == '__main__':
    main()
