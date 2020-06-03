class ReadFiles:
    def __init__(self, _file: str, txt_open_mode=None):
        self._file = _file
        self.txt_open_mode = txt_open_mode
        self.opened_file = None

    @property
    def open_txt_file_read(self):
        """
        Method to open txt file in read or readlines mode
        :return:
        """
        with open(self._file, 'r', encoding='utf8') as opened_file:
            if self.txt_open_mode == 'readlines':
                self.opened_file = opened_file.readlines()
            else:
                self.opened_file = opened_file.read()
            return self.opened_file

    @property
    def open_csv_file_read(self):
        """
        Method to open CSV file
        :return:
        """
        import csv

        opened_file = open(self._file, 'r', newline='', encoding="utf8")
        self.opened_file = csv.reader(opened_file, delimiter=';')
        return self.opened_file

    def close_csv_file(self):
        self.opened_file.close()


class ReadTxtFiles(ReadFiles):
    def __init__(self, _file: str, search_word=None, txt_open_mode='None'):
        super().__init__(self, _file)
        self._file = _file
        self.word = search_word
        self.txt_open_mode = txt_open_mode
        self.all_words_counter_dict = dict()

    def word_counter(self):
        """
        method to count word in txt file
        :return:
        """
        read_txt_file = super().open_txt_file_read
        return f'słowo "{self.word}" wystąpiło {read_txt_file.count(self.word)} w pliku {self._file}'

    @property
    def all_words_counter(self) -> dict:
        """
        method to count all words in txt file
        :return:
        """
        import re

        lines = super().open_txt_file_read
        for line in lines:
            for tmp_word in line.split(" "):
                tmp_word = re.sub(r"\W", "", tmp_word)
                self.all_words_counter_dict[tmp_word] = self.all_words_counter_dict.get(tmp_word, 0) + 1
        return self.all_words_counter_dict


class ReadCsvFile(ReadFiles):
    def __init__(self, _file: str):
        super().__init__(self, _file)
        self._file = _file
        self.jumpers = []
        self.weight = []
        self.growth = []
        self.collection_of_countries = set()
        self.sl_z = dict()
        self.sl_sr_wz = dict()
        self.lista_wz = []

    def prepare_data(self):
        """
        method to prepare data form csv file
        :return:
        """
        read_csv = super().open_csv_file_read
        for row in read_csv:
            self.jumpers.append(row)
            self.weight.append(row[5])
            self.growth.append(row[4])
            self.collection_of_countries.add(row[2])
            self.sl_z[row[2]] = self.sl_z.get(row[2], 0) + 1
            tmp_wz = [row[2], row[4]]
            self.lista_wz.append(tmp_wz)

    @property
    def waga_sk_min_max(self):
        """

        :return:
        """
        return (
            f'najlżejszy: {list(row[0] + " " + row[1] for row in self.jumpers if row[5] == min(self.weight))}\n'
            f'najcięższy: {list(row[0] + " " + row[1] for row in self.jumpers if row[5] == max(self.weight))}\n'
            f'najwyższy: {list(row[0] + " " + row[1] for row in self.jumpers if row[4] == max(self.growth))}\n'
            f'najniższy: {list(row[0] + " " + row[1] for row in self.jumpers if row[4] == min(self.growth))}'
            )

    def waga_kraj(self):
        """

        :return:
        """
        selected_country = input(f'podaj kraj: {self.collection_of_countries}:')
        return f'waga wszystkich {selected_country}: ' \
               f'{sum(list(int(row[5]) for row in self.jumpers if row[2] == selected_country))}'

    @property
    def kraj_ilu_zw(self) -> list:
        """

        :return:
        """
        result = list()
        for country, counter in sorted(self.sl_z.items(), key=lambda item: item[1], reverse=True):
            tmp_item = [country, counter]
            result.append(tmp_item)
        return result

    @property
    def kraj_ilu_zw_sr_waga(self) -> list:
        """

        :return:
        """
        result = []
        for country in self.collection_of_countries:
            tmp_item = [country,
                        len((list(filter(lambda item: item[0] == country, self.lista_wz)))),
                        sum(int(t[1]) for t in self.lista_wz if t[0] == country) /
                        len((list(filter(lambda item: item[0] == country, self.lista_wz))))]
            result.append(tmp_item)
        return result


# Pan Tadeusz
a = ReadTxtFiles('pan-tadeusz.txt', 'Tadeusz', txt_open_mode='read')
print(a.word_counter())

b = ReadTxtFiles('pan-tadeusz.txt', txt_open_mode='readlines')
for word, count in sorted(b.all_words_counter.items(), key=lambda item: item[0], reverse=False):
    print(f'{word:15} -> {count:^4} -> {len(word):^4}')

# zawodnicy
c = ReadCsvFile('zawodnicy.csv')
c.prepare_data()
print(c.waga_sk_min_max)
print(c.waga_kraj())

for kraj, liczba_zw in c.kraj_ilu_zw:
    print(f'{kraj} - {liczba_zw}')

for kraj, liczba_zw, se_waga in c.kraj_ilu_zw_sr_waga:
    print(f'{kraj} - {liczba_zw} - {se_waga:.2f}')
