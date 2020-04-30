
sklep = {
    "z": 2.01,
    "j": 3.02,
    "m": 4.99
}

magazyn = {
    "z": 10,
    "j": 10,
    "m": 10
}


print('oferta:')
for nazwa, cena in sklep.items():
    print(f'{nazwa} za {cena}: stan {magazyn[nazwa]}')

x = input('co? ')

if x in sklep.keys():
    y = float(input('ile? '))
    if y <= magazyn[x]:
        magazyn[x] = magazyn[x] - y
        print(f'do zapłaty: {y * sklep[x]:.2f}')
    else:
        print('brak na magazynie')
else:
    print('nie ma')

print('stan:')
for nazwa, ilosc in magazyn.items():
    print(f'{nazwa} : {ilosc}')

product_update_name = input('zaktualizuj produkt, podaj nazwe: ')
product_update_q = float(input('zaktualizuj produkt, podaj ilosc: '))
if product_update_name in magazyn:
    magazyn[product_update_name] += product_update_q
else:
    price_for_new = float(input("podaj cene: "))
    sklep[product_update_name] = price_for_new
    magazyn[product_update_name] = product_update_q

for nazwa, cena in sklep.items():
    print(f'{nazwa} za {cena}: stan {magazyn[nazwa]}')