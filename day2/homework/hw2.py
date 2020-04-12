# z1
example_data = 'HELLO STRANGER!'
counter = 0
first_line = ''
second_line = ''

while counter != len(example_data):
    if example_data[counter] != ' ':
        if counter %2 == 0:
            first_line = first_line + example_data[counter] + ' '
        else:
            second_line = second_line + example_data[counter] + ' '
    counter += 1

print('z1:')
print(first_line + '\n' + second_line)

# z2
example_data = 'ALA MA PSA'
counter = 0
result = ''

while counter != len(example_data):
    if counter %2 == 0:
        result = result + example_data[counter]
    else:
        result = result + example_data[counter] * 2
    counter += 1
print('z2:')
print(result)

# z3
x = 4
counter = 0
sign = '*'
print('z3')

while x != counter:
    if counter == (x - 1) or counter == 0:
        print(sign * x)
    else:
        print(sign + ' ' * (x - 2) + sign)
    counter += 1

