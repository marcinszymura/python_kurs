x = int(input('podaj pozycje dla x: '))
y = int(input('podaj pozycje dla y: '))
result = ''

if (x > 100) or (x < 0) or (y > 100) or (y < 0):
    result = 'poza planszą'
elif x <= 10:
    if y <= 10:
        result = 'w lewym dolnym rogu'
    elif y >= 90:
        result = 'w lewym górnym rogu'
    else:
        result = 'na lewej krawędzi'
elif x >= 91:
    if y <= 10:
        result = 'w prawym dolnym rogu'
    elif y >= 90:
        result = 'w prawym górnym rogu'
    else:
        result = 'na prawej krawędzi'
elif y < 10:
    result = 'na dolniej krawędzi'
elif y > 90:
    result = 'na górnej krawędzi'
    result = 'na górnej krawędzi'
else:
    result = 'w centrum'

print(f'Gracz znajduje się: {result}')
