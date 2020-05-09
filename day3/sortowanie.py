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
# for indeks_podstawienia in range(len(lista)):
#     indeks_min_wartosci = indeks_podstawienia
#     for indeks_ogona in range(indeks_podstawienia + 1, len(lista)):
#         print(lista[indeks_ogona], lista[indeks_min_wartosci])
#         if lista[indeks_ogona] < lista[indeks_min_wartosci]:
#             print(f' if {lista[indeks_ogona]} < {lista[indeks_min_wartosci]}')
#             indeks_min_wartosci = indeks_ogona
#     # a, b  = b, a
#     lista[indeks_podstawienia], lista[indeks_min_wartosci] = lista[indeks_min_wartosci], lista[indeks_podstawienia]
#     print(lista)
# assert lista == [0, 1, 2, 3, 4, 6, 8, 9]

# for i in range(len(lista)):
#     min = i
#     print(f' min {min}')
#     for x in range(i+1, len(lista)):
#          if lista[x] < lista[min]:
#             print(f'lista[x] < lista[min] {lista[x], lista[min]}')
#             min = x
#     lista[i], lista[min] = lista[min], lista[i]
#     print(lista)


lista = [9, 1, 6, 8, 4, 3, -1, 2, 0, 11, 1]
for i in range(len(lista)):
    # print(f'iteracja {i} -> {lista[i]}')
    min = i
    for x in range(i):
        if lista[i - x -1] > lista[min]:
            lista[i - x -1], lista[min] = lista[min], lista[i - x -1]
            min = i - x -1
            print(lista)

