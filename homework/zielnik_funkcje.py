produkty = {
    "ziemniaki": 2.25,
    "pomidory": 4.15,
    "cebula": 1.99,
    "kalafior": 3.20
}
magazyn = {
    "ziemniaki": 10,
    "pomidory": 10,
    "cebula": 10,
    "kalafior": 10
}


def oferta(produkty):
    print("Nasz zielnik oferuje: ")
    for nazwa, cena in produkty.items():
        print(f" - {nazwa} w cenie: {cena} PLN (stan: {magazyn[nazwa]})")


def weryfikacja_ilosci(ile, produkt):
    if ile < magazyn[produkt]:
        print(f"Za {ile} kg {produkt} zapłacisz {ile * produkty[produkt]:.2f}")
        magazyn[produkt] = magazyn[produkt] - ile
    else:
        print("Nie mamy tyle produktu")


def zakupy(produkt):
    if produkt in produkty:
        ile = input(f"Ile chcesz kupić [{produkt}]? ")
        ile = float(ile)
        weryfikacja_ilosci(ile, produkt)
    else:
        print(f'produkt {produkt}: brak w sklepie')


def aktualizacja_magazynu(produkt, ile):
    magazyn[produkt] = magazyn.get(produkt, 0) + ile
    if produkt not in produkty:
        cena = float(input(f"Jaka cena za [{produkt}]"))
        produkty[produkt] = cena


while True:
    komenda = input("Co chcesz zrobić? [k-kup] [z-zakończ] [m-magazyn]")
    if komenda == "z":
        break
    elif komenda == "k":
        oferta(produkty)
        produkt = input("Co chcesz kupić? ")
        zakupy(produkt)
    elif komenda == "m":
        produkt = input("Co dodajemy? ")
        ile = int(input(f"Ile dodajemy [{produkt}]? "))
        aktualizacja_magazynu(produkt, ile)
    else:
        print("Niezrozumiała komenda")