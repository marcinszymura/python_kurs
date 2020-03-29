number_1 = int(input('Podaj pierwsza liczbe: '))
number_2 = int(input('Podaj druga liczbe: '))
action = input('Podaj rodzaj operacji: ')

if action == '+':
    print(f'Wynik: {number_1 + number_2}')
elif action == '-':
    print(f'Wynik: {number_1 - number_2}')
elif action == '*':
    print(f'Wynik: {number_1 * number_2}')
elif action == '/' and number_2 != 0:
    print(f'Wynik: {number_1 / number_2}')
else:
    print(f'{action} nieznane dzialanie lub dzielenie przez 0')
