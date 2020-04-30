

def policz_znaki(tekst, start='<', stop='>'):
    counter = 0
    for sign in tekst:
        if sign == start:
            if sign != stop:
                counter += 1
            else:
                return counter

policz_znaki('ala ma <kota> a kot ma ale')

def test_polcz_znaki(tekst, ):
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4
