import datetime

obecny_rok = datetime.datetime.now().year
rok_urodzenia = int(input('Podaj rok urodzenia: '))
wiek = obecny_rok - rok_urodzenia

if rok_urodzenia <= 0 or rok_urodzenia > obecny_rok:
    print(f'podales bledny rok urodzenia - {rok_urodzenia}')
else:
    if obecny_rok - rok_urodzenia >=18:
        print(f'wiek: {wiek} lat, jestes pelnoletni')
    else:
        print('Jestes niepelnoletni')