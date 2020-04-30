# zadanie1
#

# bez podpowiedzi, pierwsza myśl
def can_you_tell_me_if_palindrom(word):
    if len(word) % 2 == 0:
        return False
    for i in range(len(word)):
        if word[i] == word[-1 - i]:
            continue
        else:
            return False
    return True

print(can_you_tell_me_if_palindrom('python'))
print(can_you_tell_me_if_palindrom('kajak'))

#z podowiedzią
def can_you_tell_me_if_palindrom_2(word):
    word_list = list(word)
    if word_list == word_list[::-1]:
        return True
    else:
        return False

print(can_you_tell_me_if_palindrom_2('python'))


def test_czy_palindrom():
    assert can_you_tell_me_if_palindrom('python') == False
    assert can_you_tell_me_if_palindrom('aga') == True
    assert can_you_tell_me_if_palindrom('kajak') == True


def test_czy_palindrom2():
    assert can_you_tell_me_if_palindrom_2('python') == False
    assert can_you_tell_me_if_palindrom_2('aga') == True
    assert can_you_tell_me_if_palindrom_2('kajak') == True


#zadanie2
#
def filtering(lista, min, max):
    result = []
    for i in lista:
        if i >= min and i <= max:
            result.append(i)
    return result

print(filtering([-2, 10, 0, 5, 1, 16, 9], 5, 15))

def test_filtruj():
    assert filtering([-2, 10, 0, 5, 1, 16, 9], 5, 15) == [10, 5, 9]
    assert filtering([-2, 10, 0, 5, 1, 16, 9], 11, 20) == [16]
    assert filtering([-2, 10, 0, 5, 1, 16, 9], -100, 0) == [-2, 0]
    assert filtering([-2, 10, 0, 5, 1, 16, 9], -100, 100) == [-2, 10, 0, 5, 1, 16, 9]


#zadanie_3
#
def leap_years(year_start, year_stop):
    result = []
    if year_start > year_stop:
        result.append('range error')
    for i in range(year_start, year_stop + 1, 1):
        if i % 4 == 0:
            result.append(i)
    return result

print(leap_years(1992, 2020))


def test_leap_years():
    assert leap_years(2300, 2020) == ['range error']
    assert leap_years(1990, 2020) == [1992, 1996, 2000,	2004, 2008, 2012, 2016, 2020]
    assert leap_years(1990, 1991) == []
    assert leap_years(-4, 4) == [-4, 0, 4]


#zadanie_4
def word_counter(sentence):
    result = {}
    for word in sentence.split():
        result[word] = result.get(word, 0) + 1
    return result


print(word_counter('ala ma kota i kota ma ala'))


def test_word_counter():
    assert (word_counter('ala ma kota i kota ma ala')) == {'ala': 2, 'ma': 2, 'kota': 2, 'i': 1}
    assert (word_counter('What\'s new in Python 3.8')) == {"What's": 1, 'new': 1, 'in': 1, 'Python': 1, '3.8': 1}
    assert (word_counter('a l a m a k o t a i k o t a m a a l a')) == {'a': 8, 'l': 2, 'm': 2, 'k': 2, 'o': 2, 't': 2, 'i': 1}
