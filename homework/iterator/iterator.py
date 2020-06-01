#
# Zaimplementuj iterator zwracający jedynie samogłoski z zadanego ciągu znaków:
# ​
# Przykładowe użycie:
# for char in Vowels('ala ma kota a kot ma ale'):
#


class Vowels:
    def __init__(self, sentence: str):
        self.sentence = sentence
        self.vowels = ['a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'y', ' ']

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self) -> str:
        if self.counter >= len(self.sentence):
            raise StopIteration
        for i in self.sentence:
            if i not in self.vowels:
                self.sentence = self.sentence.replace(i, '')
            self.counter += 1

        return self.sentence


for char in Vowels('ala ma kota a kot ma ale'):
    print(char)

