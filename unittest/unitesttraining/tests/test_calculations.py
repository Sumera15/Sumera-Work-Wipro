import unittest

from src.calculations import add,subtract,mul,div,ne

class TestCalculations(unittest.TestCase): #TestClass
    def test_add(self):
        res = add(10,5)
        self.assertEqual(res, 15, msg='Addition Err')

    def test_subtract(self):
        res = subtract(10,2)
        self.assertEqual(res, 8, msg='Subtraction  Err')

    def test_mul(self):
        res = mul(10,2)
        self.assertEqual(res, 20, msg='Mul  Err')

    def test_div(self):
        res = div(10, 2)
        self.assertEqual(res, 5, msg='Div  Err')

    def test_ne(self):
        res = ne(10,10)
        self.assertTrue(res, msg='NE')


