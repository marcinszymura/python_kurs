# 1. Wymień poznane dotąd struktury danych:
# lista, słownik, tuple
# int, float, bool, string


# 2. Które z nich są mutowalne a które nie?:
# mutowalne: listy, słowniki
# niemutowalne: tuple2, int, float, bool, string

# 3. Zaimplementuj funkcję realizującą algorytm sortowanie przez wybieranie

lista = [9, 1, 6, 8, 4, 3, 2, 0]

def sort(lista):
    for indeks_podstawienia in range(len(lista)):
        indeks_min_wartosci = indeks_podstawienia
        for indeks_ogona in range(indeks_podstawienia + 1, len(lista)):
             if lista[indeks_ogona] < lista[indeks_min_wartosci]:
                indeks_min_wartosci = indeks_ogona
        # a, b  = b, a
        lista[indeks_podstawienia], lista[indeks_min_wartosci] = lista[indeks_min_wartosci], lista[indeks_podstawienia]
    return lista

print(sort(lista))

