x = int(input('podaj pozycje dla x: '))
y = int(input('podaj pozycje dla y: '))
result = ''

if (0 > x > 100) or (0 > y > 100):
    result = 'poza planszą'
elif (0 <= x <= 10) and (0 <= y <= 10):
    result = 'w lewym dolnym rogu'
elif (0 <= x <= 10) and (91 <= y <= 100):
    result = 'w lewym górnym rogu'
elif (91 <= x <= 100) and (0 <= y <= 10):
    result = 'w prawym dolnym rogu'
elif (91 <= x <= 100) and (91 <= y <= 100):
    result = 'w prawym górnym rogu'
elif (0 <= x <= 10) and (11 <= y <= 90):
    result = 'na lewej krawędzi'
elif (10 <= x <= 90) and (0 <= y <= 10):
    result = 'na dolniej krawędzi'
elif (91 <= x <= 100) and (11 <= y <= 90):
    result = 'na prawej krawędzi'
elif (91 <= x <= 100) and (11 <= y <= 90):
    result = 'na górnej krawędzi'
else:
    result = 'w centrum'

print(f'Gracz znajduje się: {result}')