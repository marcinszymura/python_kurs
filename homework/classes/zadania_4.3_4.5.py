### Zadanie 4.3 | Pociąg
import pytest


class Train:
    MAX_SPEED_UPDATE = 75

    def __init__(self, speed: int, fuel_amount: float):
        self.speed = speed
        self.fuel_amount = fuel_amount

    def desc(self) -> str:
        return f'Moja predkość to {self.speed}. Mam jeszcze {self.fuel_amount} litrów paliwa.'

    def __str__(self) -> str:
        return self.desc()

    def acceleration(self, increase_speed: int) -> (int, float):
        """
        Metoda do zwiększania prędkości pociągu

        :param increase_speed:
        :return:
        """
        old_speed = self.speed
        fuel_cost = (self.speed + increase_speed - old_speed) * (old_speed / 100)
        if (self.speed < self.speed + increase_speed < self.speed * (Train.MAX_SPEED_UPDATE / 100) + self.speed) and \
                fuel_cost <= self.fuel_amount:
            self.speed += increase_speed
            self.fuel_amount -= fuel_cost
        return self.speed, self.fuel_amount


class TestTrain:
    def test_acceleration(self):
        train1 = Train(10, 1000)
        assert train1
        train1.acceleration(5)
        assert train1.desc() == 'Moja predkość to 15. Mam jeszcze 999.5 litrów paliwa.'
        train1.acceleration(20)
        assert train1.desc() == 'Moja predkość to 15. Mam jeszcze 999.5 litrów paliwa.'
        train1.acceleration(8)
        assert train1.desc() == 'Moja predkość to 23. Mam jeszcze 998.3 litrów paliwa.'
        train1.acceleration(10)
        assert train1.desc() == 'Moja predkość to 33. Mam jeszcze 996.0 litrów paliwa.'


### Zadanie 4.4 | Zbiornik
print('*' * 100)


class Zbiornik:
    def __init__(self, ilosc_wody: float, tempertaura: float):
        self.ilosc_wody = ilosc_wody
        self.tempertaura = tempertaura

    def __str__(self):
        return self.desc()

    def desc(self):
        return f'zbiornik z {self.ilosc_wody} litrami wody w temperaturze {self.tempertaura:.2f}'

    def dolej(self, ile: float, temperatura: float) -> (float, float):
        """
        Metoda oblicza ilość litrów wody w zbiorniku po dolaniu
        :param ile:
        :return:
        """
        temperatura_przed_dolaniem = self.tempertaura
        ilosc_wody_przed_dolaniem = self.ilosc_wody
        self.ilosc_wody += ile
        self.tempertaura = (ilosc_wody_przed_dolaniem * temperatura_przed_dolaniem + ile * temperatura) \
                           / self.ilosc_wody
        return self.ilosc_wody, self.tempertaura

    def odlej(self, ile: float) -> float:
        """
        Metoda oblicza ilość litrów wody w zbiorniku po odlaniu
        :param ile:
        :return:
        """
        if ile >= self.ilosc_wody:
            self.ilosc_wody = 0
        else:
            self.ilosc_wody -= ile

        return self.ilosc_wody


class TestZbiornik:
    def test_dolej(self):
        zb1 = Zbiornik(10, 5)
        zb1.dolej(10, 5)
        assert zb1.desc() == 'zbiornik z 20 litrami wody w temperaturze 5.00'
        zb1.odlej(30)
        assert zb1.desc() == 'zbiornik z 0 litrami wody w temperaturze 5.00'
        zb1.dolej(20, 15)
        assert zb1.desc() == 'zbiornik z 20 litrami wody w temperaturze 15.00'
        zb1.odlej(30)
        assert zb1.desc() == 'zbiornik z 0 litrami wody w temperaturze 15.00'


### Zadanie 4.5 | Żółw
print('*' * 100)


class Zolw:
    def __init__(self, x: int, y: int, kurs: str = 0):
        self.x = x
        self.y = y
        self.kurs = kurs

    def __str__(self):
        return f'x={self.x} y={self.y}'

    def idz(self, dystans: int):
        if self.kurs == 0:
            self.y -= dystans
        elif self.kurs == 90:
            self.x += dystans
        elif self.kurs == 180:
            self.y += dystans
        elif self.kurs == 270:
            self.x -= dystans
        return self.x, self.y

    def obroc_sie(self, kurs):
        kursy = [0, 90, 180, 270]
        if kurs not in kursy:
            raise ValueError('niewłaściwy kurs')
        self.kurs = kurs
        return self.kurs


class TestZolw:
    def test_obroc_sie(self):
        z = Zolw(100, 100)
        with pytest.raises(ValueError):
            z.obroc_sie(1)
            z.obroc_sie(175)

    def test_idz(self):
        z = Zolw(100, 100)
        z.idz(50)
        assert str(z) == 'x=100 y=50'
        z.obroc_sie(90)
        z.idz(50)
        assert str(z) == 'x=150 y=50'
        z.obroc_sie(180)
        z.idz(50)
        assert str(z) == 'x=150 y=100'
