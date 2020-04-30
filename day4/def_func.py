def liczba_pierwsza(liczba):
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True


print(liczba_pierwsza(11))

# definicja testów dla funkcji przez pytest
def test_czy_pierwsza_dla_liczby_pierwszej_true():
    assert liczba_pierwsza(17) == True
    assert liczba_pierwsza(11) == True

def test_czy_pierwsza_dla_liczby_pierwszej_false():
    assert liczba_pierwsza(16) == False
    assert liczba_pierwsza(12) == False
