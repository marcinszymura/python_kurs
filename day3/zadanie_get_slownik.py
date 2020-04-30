word = 'podaj slowo lub zdanie:'
dict1 = dict()

for sign in word:
    dict1[sign] = dict1.get(sign, 0) + 1

for znak, ilosc in dict1.items():
    print(f'{znak} -> {ilosc}')


from collections import defaultdict
zliczenia = defaultdict(int)
for znak in word:
    zliczenia[znak] += 1
print("333: ", zliczenia)