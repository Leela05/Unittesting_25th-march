import calculator

import unittest

class calculatortest(unittest.TestCase):
    def test_case1(self):
        number1 = 20
        number2 = 10
        addition = calculator.add(number1, number2)
        self.assertEqual(number1 + number2, addition)

    def test_case2(self):
        number1 = 20
        number2 = 10
        Subtraction = calculator.sub(number1, number2)
        self.assertEqual(number1 - number2, Subtraction)

    def test_case3(self):
        number1 = 20
        number2 = 10
        Multiplication = calculator.mul(number1, number2)
        self.assertEqual(number1 * number2, Multiplication)

    def test_case4(self):
        number1 = 20
        number2 = 10
        Division = calculator.div(number1, number2)
        self.assertEqual(number1 / number2, Division)

    def test_case5(self):
        number1 = 20
        number2 = 10
        Floor_Division = calculator.floordivision(number1, number2)
        self.assertEqual(number1 // number2, Floor_Division)

    def test_case6(self):
        number1 = 20
        number2 = 10
        Modulo = calculator.modulo(number1, number2)
        self.assertEqual(number1 % number2, Modulo)

    def test_case7(self):
        number1 = 20
        number2 = 10
        Exponential = calculator.exponential(number1, number2)
        self.assertEqual(number1 ** number2, Exponential)

if __name__ == "__main__":
    unittest.main()