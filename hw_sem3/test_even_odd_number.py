import unittest
from nums import even_odd_number

class TestEvenOddNumber(unittest.TestCase):
    def test_even_number(self):
        self.assertTrue(even_odd_number(8))

    def test_odd_number(self):
        self.assertFalse(even_odd_number(3))


if __name__ == '__main__':
    unittest.main(verbosity=2)