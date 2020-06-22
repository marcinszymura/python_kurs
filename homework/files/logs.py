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
    working_time = dict()
    for a in list(reader):
        working_time[a[0]] = working_time.get(a[0], 0) + int(a[1])

for user, work_time in working_time.items():
    print(f'- {user}: {work_time} s.')


### Zadanie 7.4 | Czas przebywania w systemie - wersja rozszerzona​
# Rozbuduj poprzednie zadanie. Plik z logami posiada informację o czasie logowania do systemu i o czasie wylogowania
# z systemu. Oblicz czas spędzony w systemie na podstawie informacji o tym kiedy użytkownik się logował
# do systemu i kiedy się z niego wylogowywał.


import csv

with open('logs.txt', 'r', newline='', encoding="utf8") as opened_file:
    reader = csv.reader(opened_file, delimiter=';')
    working_time = dict()
    tmp_login = dict()
    for a in list(reader):
        if a[1] == 'LOGIN':
            if a[0] not in tmp_login:
                tmp_login[a[0]] = tmp_login.get(a[0], 0) + int(a[2])
            else:
                tmp_login[a[0]] = a[2]
        else:
            working_time[a[0]] = working_time.get(a[0], 0) + (int(a[2]) - int(tmp_login[a[0]]))

for i, v in sorted(working_time.items(), key=lambda item: item[1], reverse=False):
    print(f'- {i:^10}:  {v} s.')
