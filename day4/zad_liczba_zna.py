
def more_than(example_text, counter):
    results = set()
    for sign in set(example_text):
        if example_text.count(sign) > counter:
            results.add(sign)
    return results

print(more_than('ala ma kota a kot ma ale', 2))
print(more_than('aaa bbb', 2))

def test_more_than():
    assert more_than('aaa', 2) == {'a'}
    assert more_than('aaa bbb', 2) == {'a', 'b'}