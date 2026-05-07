import pytest
from src.calculations import Calculations
class TestCalculations:
    calc = Calculations()

    @pytest.fixture()
    def setup(self):
        print('Fixture')
    @pytest.mark.parametrize('n1, n2 , exval' ,[(5,5,10),(-5,-5,-10),(0,5,5) ] )
    def test_add(self,n1,n2,exval):
        res = self.calc.add(n1, n2)
        assert res == exval, 'Addition Err'

    def test_sub(self):
        res = self.calc.subtract(10, 5)
        assert res == 5, 'Subtract Err'
    @pytest.mark.skip(reason='Not implemented yet')
    def test_mul(self):
        res = self.calc.mul(10, 5)
        assert res == 50, 'Mul Err'

    @pytest.mark.xfail(reason="division by zero not handled")
    def test_div(self):
        res = self.calc.div(10, 0)
        assert res == 0, 'Div Err'

    def test_ne(self):
        res = self.calc.ne(10, 10)
        assert res == True, 'NOT Equal'


    def test_driver(self):
        res = self.calc.div(10, 0)
        assert res == 0
