# lista = [9, 1, 6, 8, 4, 3, 2, 0]
# counter = 0
#
# wynik = lista[0]
#
# for i in lista:
#      if i < wynik:
#          wynik = i
#
# print(wynik)
#

lista = [9, 1, 6, 8, 4, 3, 2, 0]
for indeks_podstawienia in range(len(lista)):
    indeks_min_wartosci = indeks_podstawienia
    for indeks_ogona in range(indeks_podstawienia + 1, len(lista)):
        if lista[indeks_ogona] < lista[indeks_min_wartosci]:
            indeks_min_wartosci = indeks_ogona
    # a, b  = b, a
    lista[indeks_podstawienia], lista[indeks_min_wartosci] = lista[indeks_min_wartosci], lista[indeks_podstawienia]
print(lista)
assert lista == [0, 1, 2, 3, 4, 6, 8, 9]