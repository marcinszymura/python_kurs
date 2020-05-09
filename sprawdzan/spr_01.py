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

# zad4

zrodla = {"a": 10, "b":30}

for nazwa, wartosc in zrodla.items():
   print(f" nazwa: {nazwa}, wartość: {wartosc}")

# odnosnie C pewnie chodzi o uzycie get ale nie mam pomysłu na przykład :-)
# zrodla[c] = zrodla.get(c, 0)

# 5. Zdefiniuj funkcję foo ...

def foo(*args, **kwargs):
    pozycyjnych = len(args)
    kluczowych = len(kwargs)
    return pozycyjnych, kluczowych

pozycyjnych, kluczowych = foo(10, 20, a=1, b=2, c=3)
print(f'pozycyjnych: {pozycyjnych}' '\n' f'kluczowych: {kluczowych}')