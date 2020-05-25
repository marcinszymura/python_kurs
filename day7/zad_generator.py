"""
Zaimplementuj generator zwracający listę wszystkich możliwych rozgrywek
na podstawie dostarczonej listy graczy. Uwzględnij rewanże.

Przykładowe użycie:
for player_1, player_2 in tournament(['A', 'B', 'C']):
    ...

dla a, b, c
generator powinien oddawać pary graczy (w tupli)
(a,b)
(a,c)
(b,a)
(b,c)
(c,a)
(c,b)

petla zewnetrzna -> zawodnik_1
    petla wewnetrzna -> zawodnik_2
        sprawdzam czy rozni zawodnicy (zadownik_1 != zawodnik_2), jesli tak to
            yield (zawodnik_1, zawodnik_2)

"""

def tournament(gracze):
    for i in gracze:
        for j in gracze:
            if i != j:
                yield [i, j]


for i, j in tournament(['a', 'b', 'c']):
    print(i, j)

print(list(tournament(['a', 'b', 'c'])))