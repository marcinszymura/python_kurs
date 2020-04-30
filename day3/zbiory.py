zbior = set()

zbior.add(1)
zbior.add('x')

print(zbior)

for el in zbior:
    print(el)

print(dir(zbior))

a = {1, 2, 3}
b = {2, 3, 4}


print (a | b) # wszystkie obiekty w obu zbiorach
print(a & b) # czesc wspólna
print(a - b)
print(b - a)
print(a ^ b) # czesc rodzielna

print(a.pop()) # zwraca element (powiedzmy pierwszy, w zbiorze bliżej niezdefiniowany) i go usuwa!
print(a)