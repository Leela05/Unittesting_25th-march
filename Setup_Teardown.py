import calculator
import unittest

class Setup_teardown(unittest.TestCase):
    def setUp(self):
        self.number = 10
        self.number = 20

    def tearDown(self):
        self.number = 0
        self.number = 0

        def test_case1(self):

            addition = calculator.add(self.number1, self.number2)
            self.assertEqual(addition,self.number1 + self.number)

        def test_case2(self):

            Subtraction = calculator.sub(self.number1, self.number2)
            self.assertEqual(self.number1 - self.number2, Subtraction)

        def test_case3(self):

            Multiplication = calculator.mul(self.number1, self.number2)
            self.assertEqual(self.number1 * self.number2, Multiplication)

        def test_case4(self):

            Division = calculator.div(self.number1, self.number2)
            self.assertEqual(self.number1 / self.number2, Division)

        def test_case5(self):

            Floor_Division = calculator.floordivision(self.number1, self.number2)
            self.assertEqual(self.number1 // self.number2, Floor_Division)

        def test_case6(self):

            Modulo = calculator.modulo(self.number1, self.number2)
            self.assertEqual(self.number1 % self.number2, Modulo)

        def test_case7(self):

            Exponential = calculator.exponential(self.number1, self.number2)
            self.assertEqual(self.number1 ** self.number2, Exponential)

if __name__ == "__main__":
        unittest.main()