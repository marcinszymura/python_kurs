x = list(range(1, 11))
print(x)

print([el ** 3 for el in x])
print([el ** 3 for el in x if el % 2 ==0])
print({el ** 3 for el in x if el % 2 ==0}) # zbiór

print({el: el ** 3 for el in x if el % 2 ==0}) # slownik

print(tuple(el ** 3 for el in x if el % 2 ==0)) # tuple

# zadania


print([x / 10 for x in range(11)])
