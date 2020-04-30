examples = {1, 5, 101, 44, 80, 7, 99, 5, 102 }
zbior_div2 = set(range(0, 100, 2))

print(len(examples), len(zbior_div2 & examples))



elementy = ["aaa", "aaaaa", "aba", "aba", "aaa", "ababa"]
el2 = {"aaa", "aba", "ccc"}
print(el2 & set(elementy)) # elementy to lista dlatego set()



first_set = {27}
second_set = {27, 33}

print(dir(first_set))
'issubset', 'issuperset'
