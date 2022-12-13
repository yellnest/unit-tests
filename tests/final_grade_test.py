from unittest import TestCase, main

from main import final_grade


class FinalGradeTest(TestCase):
    def test_perfect_grade(self):
        self.assertEqual(final_grade(90, 9), 100)

    def test_good_grade(self):
        self.assertEqual(final_grade(85, 5), 90)

    def test_not_bad_grade(self):
        self.assertEqual(final_grade(55, 2), 75)

    def test_bad_grade(self):
        self.assertEqual(final_grade(50, 1), 0)

    def test_negative_exam(self):
        with self.assertRaises(ValueError) as e:
            final_grade(-1, 10)
        self.assertEqual('Число экзаменов не может быть меньше 0', e.exception.args[0])

    def test_negative_project(self):
        with self.assertRaises(ValueError) as e:
            final_grade(100, -10)
        self.assertEqual('Число проектов не может быть меньше 0', e.exception.args[0])


if __name__ == '__main__':
    main()
