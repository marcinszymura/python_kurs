counter = 0
week_temperature = 0
while counter < 7:
    counter += 1
    day_temperature = float(input(f'podaj temperature dla dnia {counter}: '))
    week_temperature = week_temperature + day_temperature
print(f'sr tempetatura = {float(week_temperature / counter)}')
