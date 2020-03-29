data = [2, 5, 7, 8, -1, -3, -100, 0]
higher = 0
smaller = 0
_zero = 0

for x in data:
    if x > 0:
        higher += 1
    elif x < 0:
        smaller += 1
    else:
        _zero += 1

print(f'> 0 = {higher}, < 0 = {smaller}, liczba 0 = {_zero}')
