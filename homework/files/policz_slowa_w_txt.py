### Zadanie 6.2 | Policz wybrane słowo (1 godz.)
# ​
# Plik z utworem "Pan Tadeusz" do pobrania: http://pgradzinski.students.alx.pl/kpython/pan-tadeusz.txt
# ​
# Niech program dla podanej nazwy pliku tekstowego i dla podanego słowa policzy ile razy
# to słowo występuje w pliku (np. Tadeusz w pliku `pan-tadeusz.txt`).

plik_txt = 'pan-tadeusz.txt'
slowo = 'Tadeusz'


def policz_ile(plik_txt: str, slowo: str) ->str:
    """
    funkcja do liczenia wystąpień danego słowa w pliku txt
    :param plik_txt: nazwa pliku
    :param slowo: słowo do wyszukania
    :return:
    """
    with open(plik_txt, 'r', encoding="utf8") as plik:
        w = plik.read()
    return f'słowo "{slowo}" wystąpiło {w.count(slowo)} w pliku {plik_txt}'


print(policz_ile('pan-tadeusz.txt', 'Tadeusz'))



print('*' * 50)
### Zadanie 6.2 | Policz wybrane słowo (1 godz.)
# ​
# Plik z utworem "Pan Tadeusz" do pobrania: http://pgradzinski.students.alx.pl/kpython/pan-tadeusz.txt
# ​
# Niech program dla podanej nazwy pliku tekstowego i dla podanego słowa policzy ile razy to słowo występuje w
# pliku (np. Tadeusz w pliku `pan-tadeusz.txt`).


import re


def policz_slowa(plik_txt: str) -> str:
    with open(plik_txt, 'r', encoding="utf8") as plik:
        c = 1
        counter = dict()
        while True:
            line = plik.readline()
            if not line:
                break
            for word in line.split(' '):
                word = re.sub(r"\W", "", word)
                counter[word.lower()] = counter.get(word.lower(), 0) + 1
            c += 1

    for word, count in sorted(counter.items(), key=lambda kv: kv[1], reverse=True):
        print(f'{word} -> {count}')


policz_slowa('pan-tadeusz.txt')



# ## 6. Przetwarzanie plików
# ​
# ### Zadanie 6.1 | Dane skoczków narciarskich (3 godz.)
# ​
# Plik CSV z danymi: http://pgradzinski.students.alx.pl/kpython/zawodnicy.csv
# ​
# Korzystając z pliku CSV z danymi skoczków narciarskich napisz programy, które wczytują ten plik i:
# ​
# 1. wypisuje najwyższego, najwyższego, najcięższego i najlżejszego skoczka;
# gdyby kilku miało taką samą wagę lub wzrost, to wystarczy wypisać jednego z nich.
# 2. liczy ile łącznie ważą reprezentanci Polski (np. żeby sprawdzić czy zmieszczą się w windzie na skocznię ;)).
# Pozwól użytkownikowi podać kraj (niekoniecznie musi być Polska).
# 3. (trudniejsze) dla wszystkich krajów oblicza ilu jest zawodników z tego kraju; tzn. ma się wypisać,
# być może w innej kolejności:



import csv


with open('zawodnicy.csv', 'r', newline='', encoding="utf8") as plik_csv:
    read_csv = csv.reader(plik_csv, delimiter=';')
    zawodnicy = []
    waga = []
    wzrost = []
    kraj = set()
    lista_z = dict()
    sl_sr_wz = dict()
    lista_wz = []
    for row in read_csv:
        zawodnicy.append(row)
        waga.append(row[5])
        wzrost.append(row[4])
        kraj.add(row[2])
        lista_z[row[2]] = lista_z.get(row[2], 0) + 1
        # sl_sr_wz[row[2]] = [sl_sr_wz.get(row[2], 0) + int(row[4]), sl_sr_wz.get(row[2], 0) + 1]
        # sl_sr_wz[row[2]] = sl_sr_wz.get(row[2], 0) + [200, 1]
        tmp_wz = [row[2], row[4]]
        lista_wz.append(tmp_wz)
# 1
print(f'najlżejszy: {list(row[0] + " " + row[1] for row in zawodnicy if row[5] == min(waga))}')
print(f'najcięższy: {list(row[0] + " " + row[1] for row in zawodnicy if row[5] == max(waga))}')
print(f'najwyższy: {list(row[0] + " " + row[1] for row in zawodnicy if row[4] == max(wzrost))}')
print(f'najniższy: {list(row[0] + " " + row[1] for row in zawodnicy if row[4] == min(wzrost))}')

# 2
# kraj_z = input(f'podaj kraj: {kraj}:')
# print(f'waga wszystkich {kraj_z}: {sum(list(int(row[5]) for row in zawodnicy if row[2] == kraj_z))}')

# 3
for kraj, liczba in sorted(lista_z.items(), key=lambda item: item[1], reverse=True):
    print(f'{kraj} - {liczba}')

# 4

print(lista_wz)
test = len(list(filter(lambda a: a[0] == 'POL', lista_wz)))
test1 = sum(list(filter(lambda i: int(i[1]) if i[0] == 'POL' else None, lista_wz)))
print(test)
print(test1)




# print(sl_sr_wz)
# print(lista_z)
# tmp = list(k, lista_z[k], sl_sr_wz[k] / int(lista_z[k]) for k in sl_sr_wz)
# print(tmp)
