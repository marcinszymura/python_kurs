

plik  = open('test.txt', 'a')
plik.write('ala ma kota3\n')
plik.close()


plik = open('test.txt')
zaw = plik.read()
print(zaw)
plik.close()


plik = open('test.txt')
zaw = plik.readline()
print(zaw)
plik.close()