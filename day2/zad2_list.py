
numbers_list = []
while True:
    numbers = int(input("podaj liczbe: "))
    numbers_list.append(numbers)
    if len(numbers_list) == 10:
        break
    # print(numbers_list)
    # print(sum(numbers_list))
print(f'sr = {sum(numbers_list) / len(numbers_list)}')
