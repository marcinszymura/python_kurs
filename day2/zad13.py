
counter = 1
week_temperature = 0
while counter < 8:
    day_temperature = float(input(f'podaj temperature dla dnia {counter}: '))
    week_temperature = week_temperature + day_temperature
    counter += 1
print(f'sr tempetatura = {float(week_temperature / 7 )}')
