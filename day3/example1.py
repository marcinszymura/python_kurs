# numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for x in numbers_list:
#     print()
#     for y in numbers_list:
#         print(y, end=' ')
#         print(f'{y*x:2}', end=' ')


for i in range(10):
    print(f"{i:4}", end = "")
print()
print()
for i in range(10):
    print(i, end="    ")
    for j in range(10):
        print(f'{i*j:4}', end='')