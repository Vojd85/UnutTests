import unittest
from nums import number_in_interval


class TestNumberInInterval(unittest.TestCase):
    def test_number_less_25(self):
        self.assertFalse(number_in_interval(12))
        
    def test_number_more_100(self):
        self.assertFalse(number_in_interval(142))

    def test_number_25(self):
        self.assertFalse(number_in_interval(25))

    def test_number_100(self):
        self.assertFalse(number_in_interval(100))

    def test_number_in_interval(self):
        self.assertTrue(number_in_interval(44))


if __name__ == '__main__':
    unittest.main(verbosity=2)