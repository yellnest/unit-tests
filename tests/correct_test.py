from unittest import TestCase, main

from main import correct


class CorrectTest(TestCase):
    def test_5(self):
        self.assertEqual(correct('PARI5'), 'PARIS')

    def test_1(self):
        self.assertEqual(correct('DUBL1N'), 'DUBLIN')

    def test_0(self):
        self.assertEqual(correct('L0ND0N'), 'LONDON')


if __name__ == '__main__':
    main()
