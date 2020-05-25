

class Counter:
    def __init__(self, limit):
        self.limit = limit


    def __iter__(self):
        self.ile_oddano = 0
        return self

    def __next__(self):
        if self.ile_oddano >= self.limit:
            raise StopIteration
        wynik = self.ile_oddano
        self.ile_oddano += 1
        return wynik


c1 = Counter(5)

for liczba in c1:
    print(liczba)