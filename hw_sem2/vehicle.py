from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, company, model, year_release, num_wheels, speed):
        self._company = company
        self._model = model
        self._year_release = year_release
        self._num_wheels = num_wheels
        self._speed = speed

    @abstractmethod
    def test_drive(self):
        pass

    @abstractmethod
    def park(self):
        pass

    @property
    def company(self):
        return self._company

    @property
    def model(self):
        return self._model

    @property
    def year_release(self):
        return self._year_release

    @property
    def num_wheels(self):
        return self._num_wheels

    @property
    def speed(self):
        return self._speed

class Car(Vehicle):
    def __init__(self, company, model, year_release, num_wheels=4, speed=0):
        super().__init__(company, model, year_release, num_wheels, speed)

    def test_drive(self):
        self._speed = 60

    def park(self):
        self._speed = 0

    def __str__(self):
        return f'Машина: модель {self._model}, производитель {self._company}, выпуск {self._year_release}'
    

class Motorcycle(Vehicle):
    def __init__(self, company, model, year_release, num_wheels=2, speed=0):
        super().__init__(company, model, year_release, num_wheels, speed)

    def test_drive(self):
        self._speed = 75

    def park(self):
        self._speed = 0

    def __str__(self):
        return f'Мотоцикл: модель {self._model}, производитель {self._company}, выпуск {self._year_release}'