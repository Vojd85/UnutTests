import unittest
from calculator import calculate_discount

class TestCalculator(unittest.TestCase):
    def test_not_number(self):
        self.assertRaisesRegex(ArithmeticError, 'Значения должны быть числами', calculate_discount, 300, '10')

    def test_normal(self):
        self.assertEqual(80.0, calculate_discount(100, 20))

    def test_zero_res(self):
        self.assertEqual(0, calculate_discount(0, 20))

    def test_zero_disc(self):
        self.assertEqual(300, calculate_discount(300, 0))

    def test_order_less_null(self):
        self.assertRaisesRegex(ArithmeticError, 'Сумма покупки не может быть меньше нуля', calculate_discount, -12, 25)

    def test_disc_less_null(self):
        self.assertRaisesRegex(ArithmeticError, 'Скидка не может быть меньше нуля', calculate_discount, 300, -23)

    def test_disc_more_100(self):
        self.assertRaisesRegex(ArithmeticError, 'Скидка не может быть больше 100%', calculate_discount, 300, 160)


if __name__ == '__main__':
    unittest.main(verbosity=2)