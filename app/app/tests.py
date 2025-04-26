from django.test import SimpleTestCase

from . import calc


class CalcTests(SimpleTestCase):

    def test_add_numbers(self) -> None:
        wanted: int = 5
        recieved: int = calc.add(3, 2)
        self.assertEqual(wanted, recieved)

    def test_subtract_numbers(self) -> None:
        res: int = calc.subtract(5, 1)

        self.assertEqual(res, 4)
