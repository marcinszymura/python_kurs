def vowels(sentence: str) -> str:
    """
    method to remove consonants in sentence
    :param sentence:
    :return:
    """
    vowels = ['a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'y', ' ']
    for i in sentence:
        if i not in vowels:
            sentence = sentence.replace(i, '')
    yield sentence


for char in vowels('ala ma kota a kot ma ale'):
    print(char)
