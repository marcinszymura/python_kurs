# napisy jako kolekcje
# indeksowanie od 0

test = 'Koronawirus'
print(dir(test))
print(test.index('K'))
print(test[5])
# print(test.index('k'))    #blad
print(test[-1])             # ostatni znak jak się poda -1, -2 przedostatni itd
print(test.index('o'))      # poda index tylko pierwszy napodkany
print(test[3:7])             #zakres index