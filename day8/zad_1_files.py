import sys

try:
    file_name: str = sys.argv[1]

    with open(file_name) as file:
        data = file.read()

    print(data)

except FileNotFoundError:
    print(f'nie znaleziono pliku: {file_name}')
    exit(1)

except IndexError:
    print(f'usage: python zas_1_files.py nazwa_pliku')
    exit(1)