# def zlacz_teksty(*args, **kwargs):
#     #print(args)
#     #print(kwargs)
#     text = "\n".join(args)
#     for k, v in kwargs.items():
#         text = text.replace(k, str(v))
#     return text
# slownik = dict(x=10, y=20)
# print(slownik)
# zlacz_teksty(t1, t2, t3, x=1, y=2, z=10)
# zlacz_teksty(t1, t3)
# print("-"*40)
# print(zlacz_teksty(t1, "xxx", y=10))
# print("-"*40)
# print(zlacz_teksty(t1, "xxx", x=10))
#
# formatuj('koszt $cena PLN','kwota $cena brutto',cena=10 )
# 'koszt 10 PLN\nkwota 10 brutto'

def replace_string(*args, **kwargs):
    text = '\n'.join(args)
    for k, v in kwargs.items():
        text = text.replace('$' + k, str(v))
    return text


print(replace_string('koszt $cena PLN', 'kwota $cena brutto', cena=10))
print('-'*40)
print(replace_string('koszt $cena PLN', 'kwota $cena brutto'))
print('-'*40)
print(replace_string('koszt $cena PLN', x=20))


def test_replace_string():
    assert replace_string('koszt $cena PLN','kwota $cena brutto',cena=10 ) == 'koszt 10 PLN\nkwota 10 brutto'
    assert replace_string('koszt $cena PLN', 'kwota $cena brutto') == 'koszt $cena PLN\nkwota $cena brutto'
    assert replace_string('koszt $cena PLN', cena=20) == 'koszt 20 PLN'
