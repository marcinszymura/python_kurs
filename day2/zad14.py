

min_number = None
max_number = None

while True:
    x = input('Podaj liczbe lun naciśnij e aby zakończyć: ')
    if x == 'e':
        break
    if min_number is None:
        min_number = x
    if max_number is None:
        max_number = x
    if x < min_number:
        min_number = x
    if x > max_number:
        max_number = x
print(f'min: {float(min_number):.2f} max: {float(max_number):.2f}')
