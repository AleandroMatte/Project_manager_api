'''
Sample tests
'''

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):

    '''testa os metodos da calc'''
    def test_add_numb(self):
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numb(self):
        res = calc.subtract(35, 10)
        self.assertEqual(res, 25)
