import unittest
from multiply import multiply_3_numbers
# each test has to start with test_
class Test3Multiply(unittest.TestCase):

    def test_1(self):
        num1 = 2
        num2 = 4
        num3 = 6
        result = multiply_3_numbers(num1, num2, num3)
        self.assertEqual(result, 48)

    def test_2(self):
        num1 = -2
        num2 = -4
        num3 = -6
        result = multiply_3_numbers(num1, num2, num3)
        self.assertEqual(result, -48)

    def test_3(self):
        num1 = 25.5
        num2 = 8.6
        num3 = 9
        result = multiply_3_numbers(num1, num2, num3)
        self.assertAlmostEqual(result, 1973.7)
    
    def test_4(self):
        num1 = 25789.5
        num2 = 81234.6
        num3 = 96756
        result = multiply_3_numbers(num1, num2, num3)
        self.assertAlmostEqual(result, 202703792589025.22, 2)
    
    def test_5(self):
        num1 = 1
        num2 = 1
        num3 = 1
        result = multiply_3_numbers(num1, num2, num3)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()