# Przykład
# użycia:
# >> > przytnij(
#     data=[1, 2, 3, 4, 5, 6, 7],
#     start=lambda x: x > 3,
#     stop=lambda x: x == 6,
# )
#
# [4, 5, 6]

def przytnij(data, start, stop):
    first = list(filter(start, data))
    last = list(filter(stop, data))
    return [a for a in first if a <= last[0]]


print(przytnij(
    data=[1, 2, 3, 4, 5, 6, 7],
    start=lambda x: x > 3,
    stop=lambda x: x == 6))

print('*' * 50)
# Zaimplementuj zestaw dekoratorów otaczających zwracany przez funkcję napis tagami HTML (pogrubienie, podkreślenie, przekreślenie):
#
# Przykład użycia:
# @bold
# @italic
# def foo(arg):
#     return f'To jest {arg}'

def bold(func):
    def add_bold(*args, **kwargs):
        return '<b>' + func(*args, **kwargs) + '</b>'
    return add_bold


def italic(func):
    def add_italic(*args, **kwargs):
        return '<i>' + func(*args, **kwargs) + '</i>'
    return add_italic


def underline(func):
    def add_underline(*args, **kwargs):
        return '<u>' + func(*args, **kwargs) + '</u>'
    return add_underline

@underline
@italic
@bold
def foo(arg):
    return f'To jest {arg}'


print(foo('dekorator'))

print('*' * 50)
# Zaimplementuj dekorator wypisujący wywołanie danej funkcji (nazwa i argumenty) oraz czas jej wykonania.
#
# Przykład użycia:
# @log
# def foo(arg):
#     return f'To jest {arg}'


import time


def log(func):
    def add_log(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        stop = time.time()
        return f'{func.__name__}: czas wykonania: {stop - start:.2f}'
    return add_log


@log
def foo(arg):
    return f'To jest {arg}'

print(foo('logowanie'))