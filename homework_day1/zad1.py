# ### Zadanie 1.1 | Interakcja i proste obliczenia (ok. 2 godz.)
# ​
# Napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków. Niech program
# policzy i wyświetli, ile trzeba będzie zapłacić za pięć kilo ziemniaków.
# ​
# Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał,
# ile kosztuje kilo ziemniaków i ile kilo chce kupić.
# Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki.
# ​
# Potem napisz program, który prosi użytkownika (przez `input()`),
# żeby podał, ile kosztuje kilo ziemniaków, ile kilo ziemniaków chce kupić,
# ile kosztuje kilo bananów i ile kilo bananów chce kupić.
# Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki i banany razem.
# I niech program sprawdzi i powie, za co trzeba będzie zapłacić więcej - za banany czy za ziemniaki.


cena_za_kilo = float(input('podaj cene za kilo: '))
ilosc = float(input('podaj ilosc do zakupu:'))

print(f'cena za kilo = {cena_za_kilo} a cena za 5kg = {cena_za_kilo * 5}')
print(f'cena za kilo = {cena_za_kilo} a cena za 5kg = {cena_za_kilo * ilosc}')
