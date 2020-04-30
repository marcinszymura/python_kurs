print(dict())

# pol_ang = dict()
# pol_ang['pies'] = 'dog'
pol_ang = {
    "kot": "cat",
    "ptak": "bird"
}

dict_2 = dict(a=10, b=22, c=33)
dict_3 = dict([
    ['x', 'ala'],
    ['y', 'kot']
])

print(pol_ang)
print(dict_2, dict_3)

print(dir(dict_3))

print(dict_3.keys())
print(dict_3.values())
print(dict_3.items())


print(dict_3.get('x'))
print(dict_3.get('z', 'brak'))

if 'z' in dict_3:
    print(dict_3['z'])
else:
    print(dict_3.get('z', 0)) #-> get po przecinku nadaje wartośc zamiast default=None



# keys - wszystkie klucz
# values - wartości
# items - pary keys values