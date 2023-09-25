import unittest
from vehicle import Car, Motorcycle, Vehicle

class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.car = Car('Ford', 'C-Max', 2008)
        self.moto = Motorcycle('Honda', 'MagnaV45', 1988)

    def test_car_is_vehicle(self):
        self.assertTrue(isinstance(self.car, Vehicle))

    def test_car_with_four_wheels(self):
        self.assertEqual(self.car.num_wheels, 4)

    def test_moto_with_two_wheels(self):
        self.assertEqual(self.moto.num_wheels, 2)

    def test_car_speed_test_drive(self):
        self.car.test_drive()
        self.assertEqual(self.car.speed, 60)

    def test_moto_speed_test_drive(self):
        self.moto.test_drive()
        self.assertEqual(self.moto.speed, 75)

    def test_car_speed_parking_after_test_drive(self):
        self.car.test_drive()
        self.car.park()
        self.assertEqual(self.car.speed, 0)
        
    def test_moto_speed_parking_after_test_drive(self):
        self.moto.test_drive()
        self.moto.park()
        self.assertEqual(self.moto.speed, 0)

    
if __name__ == '__main__':
    unittest.main(verbosity=2)