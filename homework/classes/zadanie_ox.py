### Zadanie 4.6 | Kółko i krzyżyk
import random


class PlanszaXO:
    def __init__(self):
        self.x = None
        self.y = None
        self.rodzaj_elementu = None
        self.ruchy = ['11', '12', '13', '21', '22', '23', '31', '32', '33']
        self.zwyciestwa = \
            [
            [self.ruchy[2], self.ruchy[5] ,self.ruchy[8]],
            [self.ruchy[1], self.ruchy[4], self.ruchy[7]],
            [self.ruchy[0], self.ruchy[3], self.ruchy[6]],
            [self.ruchy[2], self.ruchy[1], self.ruchy[0]],
            [self.ruchy[5], self.ruchy[4], self.ruchy[3]],
            [self.ruchy[8], self.ruchy[7], self.ruchy[6]],
            [self.ruchy[2], self.ruchy[4] ,self.ruchy[6]],
            [self.ruchy[0], self.ruchy[4], self.ruchy[8]]
            ]

    def __str__(self):
        return self.desc()

    def desc(self):
        desc = f'{self.ruchy[2]}|{self.ruchy[5]}|{self.ruchy[8]}\n' \
               f'{self.ruchy[1]}|{self.ruchy[4]}|{self.ruchy[7]}\n' \
               f'{self.ruchy[0]}|{self.ruchy[3]}|{self.ruchy[6]}'
        return desc

    def kto_zaczyna(self):
        self.rodzaj_elementu = random.choice(['o', 'x'])
        return self.rodzaj_elementu

    def dodaj_element(self, x: int, y: int):
        self.x = x
        self.y = y
        ruch = str(self.x) + str(self.y)
        if ruch in self.ruchy:
            tmp_index = self.ruchy.index(ruch)
            self.ruchy[tmp_index] = self.rodzaj_elementu + ' '
        else:
            return False

        for kombinacja in self.zwyciestwa:
            if ruch in kombinacja:
                tmp_index2 = kombinacja.index(ruch)
                kombinacja[tmp_index2] = self.rodzaj_elementu
        return self.ruchy, self.zwyciestwa

    def stan_gry(self):
        for kombinacja in self.zwyciestwa:
            if kombinacja.count('x') == 3:
                return 'gra zakończona, sukces krzyżyków'
            elif kombinacja.count('o') == 3:
                return 'gra zakończona, sukces kółek'
        if self.ruchy.count('o ') + self.ruchy.count('x ') < len(self.ruchy):
           return 'gra trwa'
        else:
            return 'koniec gry, brak zwycięzcy'

    def czyj_ruch(self):
        if self.rodzaj_elementu == 'o':
            self.rodzaj_elementu = 'x'
        else:
            self.rodzaj_elementu = 'o'
        return self.rodzaj_elementu


## gramy:
gra = PlanszaXO()
print(gra)
print(f'Gramy, zaczynają: {gra.kto_zaczyna()}')
while True:
    x, y = input('podaj współrzędne xy:')
    while gra.dodaj_element(x, y) is False:
        print(f'ruch {str(x) + str(y)} został już wykorzystany')
        x, y = input('podaj nowe współrzędne xy:')
    print(gra)
    print(gra.stan_gry())
    if 'sukces' in gra.stan_gry() or 'koniec' in gra.stan_gry():
        exit()
    print(f'ruch dla: {PlanszaXO.czyj_ruch(gra)}')
