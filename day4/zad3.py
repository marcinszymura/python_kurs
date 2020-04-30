

def policz_znaki(text, start='<', stop='>'):
    poziom = 0
    counter = 0
    state = False
    for sign in text:
        if sign == start:
            poziom += 1
            state = True
            continue
        elif sign == stop:
            poziom -=1
            state = False
        if state:
            counter += poziom
    return counter

print(policz_znaki('ala ma <kota> a kot ma ale'))
print(policz_znaki('ala ma [kota] a [kot] ma ale', '[', ']'))
print(policz_znaki('ala ma <ko>ta a kot ma ale'))
print(policz_znaki('ala ma <kota> a <kot> ma ale'))
print(policz_znaki('a <a<a<a>>>'))

def test_polcz_znaki():
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4
    assert policz_znaki('ala ma <ko>ta a kot ma ale') == 2
    assert policz_znaki('ala ma <kota> a <kot> ma ale') == 7
    assert policz_znaki('ala ma [kota] a [kot] ma ale', "[", "]") == 7
    assert policz_znaki('a <a<a<a>>>') == 6

