# x = (1 , 2 , 100, '123str')
#
# print(len(x))
# print(x.count(100))
#
# print(x[0])
# print(x[:3])
# print(x[::2])
#

#zad
y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
# print co drugi element
print(y[::2])
# print przedostatni
print(y[-2])
# print od 3 do 7
print(y[2:7])
# print co trzeci element
print(y[::3])
# print co drugi element od końca
print(y[::-2])

for i in y:
    print(i)

print(tuple('123456'))
