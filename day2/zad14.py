

min_number = None
max_number = None

while True:
    x = input('Podaj liczbe lun naciśnij e aby zakończyć: ')
    if x == 'e':
        break
    x = float(x)
    if min_number is None or x < min_number:
        min_number = x
    if max_number is None or x > max_number:
        max_number = x

print(f'min: {float(min_number):.2f} max: {float(max_number):.2f}')
