from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        wanted = 5
        recieved = calc.add(3,2)
        self.assertEqual(wanted, recieved)
