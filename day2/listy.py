# ele = [1, 2, 3, 4, 5, 6, 'test']
#
# print(dir(ele))
#
# # 'append', 'clear', 'copy', 'count',
# # 'extend', 'index', 'insert', 'pop',
# # 'remove', 'reverse', 'sort'
# #  len działa jak w reszcie


days_week = ['PN', 'WT', 'SR', 'CZW', 'PT', 'S', 'N']

counter = 0
while counter <= 10:
    print(f'{counter}, {days_week[counter % 7]}, za dwa dni -> {days_week[(counter + 2) % 7]}')
    counter += 1

