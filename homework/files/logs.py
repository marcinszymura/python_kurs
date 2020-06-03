# ### Zadanie 7.3 | Czas przebywania w systemie - wersja podstawowa
# ​
# Napisz program wczytujący plik z logami aktywności użytkowników w systemie.
# Na podstawie wczytanych danych wyświetl informację o sumarycznym czasie
# przebywania każdego użytkownika w systemie.
# ​
# $ python read_logs.py logs_simple.txt
# Czas przebywania w systemie:
# - user-1: 92 s
# - user-2: 51 s
# - user-3: 20 s

import csv

with open('logs_simple.txt', 'r', newline='', encoding="utf8") as opened_file:
    reader = csv.reader(opened_file, delimiter=';')
    result = dict()
    for a in list(reader):
        result[a[0]] = result.get(a[0], 0) + int(a[1])

for user, work_time in result.items():
    print(f'- {user}: {work_time} s.')
