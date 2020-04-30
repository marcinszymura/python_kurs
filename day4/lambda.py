lista_osob = ['Jan Nowak', 'Anna Zagajska', 'Piotr Baron', 'Aron Aron']

print(sorted(lista_osob, key=lambda x: x.split()[1]))

y = 'Jan Nowak'
print(y.split()[1])







def silnia(n):
    if n == 0:
        return 1
    elif n < 0:
        print('error')
    else:
        return n * silnia(n - 1)


print(silnia(5))

def test_silnia():
    silnia(5) == 120
    silnia(0) == 1
    silnia(1) == 1
    silnia(2) == 4
    silnia(-1) == 'error'




def recu_print(text):
    # nie można użyć petli
    pass