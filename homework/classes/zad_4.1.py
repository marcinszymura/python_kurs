class Ogloszenie:
    def __init__(self, tytul: str, opis: str, cena: float, dane_kontaktowe: str):
        self.tytul = tytul
        self.opis = opis
        self.cena = cena
        self.dane_konatktowe = dane_kontaktowe

    def __str__(self) -> str:
        return f'Tytul: {self.tytul}, opis: {self.opis}, cena: {self.cena}, dane kontaktowe: {self.dane_konatktowe}'

        def dodaj_ogłoszenie(self):
            pass


o1 = Ogloszenie('Sprzedam koze', 'koza, wiek 4 lata', 250.0, 'Marian, 7778888999')
o2 = Ogloszenie('Sprzedam kota', 'kot, dachowiec, wiek 1,5', 12.5, 'Krystyna, 222333444')
o2 = Ogloszenie('Sprzedam psa', 'pies, z rodowodem, wiek 0,5', 550.0, 'Krystyna, 222333444')


print(o1)
print(o2)


class OgloszenieSamochodowe(Ogloszenie):
    def __init__(self,
                 tytul: str,
                 opis: str,
                 cena: float,
                 dane_kontaktowe: str,
                 model: str,
                 marka: str,
                 rok_prod: int,
                 przebieg: int,
                 pojemnosc: float,
                 moc: int,
                 rodzaj_paliwa: str
                 ):
        super().__init__(tytul, opis, cena, dane_kontaktowe)
        self.model = model
        self.marka = marka
        self.rok_prod = rok_prod
        self.przebieg = przebieg
        self.pojemnosc = pojemnosc
        self.moc = moc
        self.rodzaj_paliwa = rodzaj_paliwa


    def __str__(self):
        return f'{super().__str__()} \nModel: {self.model}'


car1 = OgloszenieSamochodowe('Sprzedam samochód', 'sprowadzony', 15000.00, 'Zbyszek, 123123123', 'superb', 'skoda', 2008, 190200, 2.2,
    1980, 'benzyna')

print(car1)
