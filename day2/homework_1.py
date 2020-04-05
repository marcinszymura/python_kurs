x = int(input('podaj pozycje dla x: '))
y = int(input('podaj pozycje dla y: '))
result = ''

if (0 <= x <= 100) and (0 <= y <= 100):
    if y <= 10:
        if x <= 10:
            result = 'w lewym dolnym rogu'
        elif (x > 10) and (x <= 90):
            result = 'na dolniej krawędzi'
        else:
            result = 'w prawym dolnym rogu'

    if (y > 10) and (y <= 90):
        if x <= 10:
            result = 'na lewej krawędzi'
        elif (x > 10) and (x <= 90):
            result = 'w centrum'
        else:
            result = 'na prawej krawędzi'

    if y > 90:
        if x <= 10:
            result = 'w lewym górnym rogu'
        elif (x > 10) and (x <= 90):
            result = 'na górnej krawędzi'
        else:
            result = 'w prawym górnym rogu'
else:
    result = 'poza planszą'

print(f'Gracz znajduje się: {result}')