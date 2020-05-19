class ElectricCar:
    def __init__(self, max_distance):
        self._traveled_distance = 0
        self.max_distance = max_distance

    def drive(self, distance):
        if distance <= (self.max_distance - self._traveled_distance):
            self._traveled_distance += distance
            return distance
        else:
            to_travel = self.max_distance - self._traveled_distance
            self._traveled_distance = self.max_distance
            return to_travel

    def charge(self):
        self._traveled_distance = 0


class TestElectricCar:
    def test_init(self):
        car = ElectricCar(100)
        assert car
        assert car.max_distance == 100

    def test_car_drive(self):
        car = ElectricCar(100)
        assert car.drive(70) == 70
        assert car.drive(50) == 30

    def test_car_charge(self):
        car = ElectricCar(100)
        assert car.drive(70) == 70
        assert car.drive(50) == 30
        car.charge()
        assert car._traveled_distance == 0
        assert car.drive(60) == 60
        assert car.drive(20) == 20
        assert car.drive(20) == 20
        assert car.drive(10) == 0