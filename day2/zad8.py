wysokosc = int(input("Podaj wysokosc: "))
szerokosc = int(input("Podaj szerokosc: "))
dlugosc = int(input("Podaj dlugosc: "))
objetosc = wysokosc * szerokosc * dlugosc
print(f"""
objetosc wynosi: {objetosc}cm3. Czy jest większa od 1l: {objetosc > 1000}
""")
