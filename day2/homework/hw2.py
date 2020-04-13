print('z1 ' + '-' * 20)
example_data = 'HELLO STRANGER!'
counter = 0
first_line = ''
second_line = ''

while counter != len(example_data):
    if example_data[counter] != ' ':
        if counter % 2 == 0:
            first_line = first_line + example_data[counter] + ' '
        else:
            second_line = second_line + example_data[counter] + ' '
    counter += 1

print(first_line + '\n' + second_line)

print()
print('z2 ' + '-' * 20)
example_data = 'ALA MA PSA'
counter = 0
result = ''

while counter != len(example_data):
    if counter % 2 == 0:
        result = result + example_data[counter]
    else:
        result = result + example_data[counter] * 2
    counter += 1
print(result)

print()
print('z3 ' + '-' * 20)
x = 4
counter = 0
sign = '*'

while x != counter:
    if counter == (x - 1) or counter == 0:
        print(sign * x)
    else:
        print(sign + ' ' * (x - 2) + sign)
    counter += 1

print()
print('z4 ' + '-' * 20)
x = 3
counter = 0
l = []

while counter != x:
    l.append(counter * 2)
    counter += 1

counter = 0
while counter != x * 2:
    if counter < x:
        print(' ' * (x - 1 - counter) + '/' + ' ' * (l[counter]) + '\\')
    else:
        print(' ' * (counter - x) + '\\' + ' ' * (l[x - 1 - counter]) + '/')
    counter += 1

print()
print('z5 ' + '-' * 20)
example_data_z5 = 'HELLO STRANGER                           !'
len_data = len(example_data_z5)
sample_sign = '*'

first_last_line = sample_sign * (len_data + 8)
data_line = sample_sign + ' ' * 3 + example_data_z5 + ' ' * 3 + sample_sign
print(first_last_line + '\n' + data_line + '\n' + first_last_line)

print()
print('z6 ' + '-' * 20)

x = 5
counter = 0
sample_sign = '*'
space_list_counter = []

for i in range(1, x *2, 2):
    space_list_counter.append(i)

while counter != x:
    if counter == 0:
        print(sample_sign)
    elif counter == x - 1:
        print(sample_sign + ' *' * (x - 1))
    else:
        print(sample_sign + ' ' * (space_list_counter[counter - 1]) + sample_sign)
    counter += 1


print()
print('z9 ' + '-' * 20)

figures = ['zero', 'jeden', 'dwa', 'trzy', 'cztery', 'pięć', 'sześć', 'siedem', 'osiem', 'dziewieć']

sample_data_z9 = '123453'
print(sample_data_z9 + ' to ', end='')
for i in sample_data_z9:
    print(figures[int(i)], end=' ')