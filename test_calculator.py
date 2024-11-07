import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def testadd1(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    #Add the following test methods to the TestCalculator class:

    def testadd2(self):
        self.assertEqual(self.calc.add(1, 1), 2)

    def testsubtract1(self):
        self.assertEqual(self.calc.subtract(2, 4), 2)
    def testsubtract2(self):
        self.assertEqual(self.calc.subtract(4, 2), -2)

    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(2, 4), 8)
    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(0, 2), 0)

    def test_divide1(self):
        self.assertEqual(self.calc.divide(4, 2), 2)
    def test_divide2(self):
        self.assertEqual(self.calc.divide(50, 5), 10)

    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(9, 3), 0)
    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

if __name__ == '__main__':
    unittest.main()