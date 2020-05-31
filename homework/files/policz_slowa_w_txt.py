class ReadFiles:
    def __init__(self, _file: str, txt_openmode=None):
        self._file = _file
        self.txt_openmode = txt_openmode
        self.opened_file = ''


    @property
    def open_txt_file_read(self):
        """
        Method to open txt file in read mode
        :return:
        """
        with open(self._file, 'r', encoding='utf8') as opened_file:
            if self.txt_openmode == 'readlines':
                self.opened_file = opened_file.readlines()
            else:
                self.txt_opened_file = opened_file.read()
            return self.opened_file

    @property
    def open_csv_file_read(self):
        """

        :return:
        """
        import csv

        opened_file = open(self._file, 'r', newline='', encoding="utf8")
        self.opened_file = csv.reader(opened_file, delimiter=';')
        return self.opened_file

    def close_csv_file(self):
        close(self._file)

class ReadTxtFiles(ReadFiles):
    def __init__(self, _file: str, word=None, txt_openmode='None'):
        super().__init__(self, _file)
        self._file = _file
        self.word = word
        self.txt_openmode = txt_openmode
        self.all_words_counter_dict = dict()

    def word_counter(self):
        read_txt_file = super().open_txt_file_read
        return f'słowo "{self.word}" wystąpiło {read_txt_file.count(self.word)} w pliku {self._file}'

    @property
    def all_words_counter(self) -> dict:
        import re

        lines = super().open_txt_file_read
        for line in lines:
            for word in line.split(" "):
                word = re.sub(r"\W", "", word)
                self.all_words_counter_dict[word] = self.all_words_counter_dict.get(word, 0) + 1
        return self.all_words_counter_dict


class ReadCsvFile(ReadFiles):
    def __init__(self, _file: str):
        super().__init__(self, _file)
        self._file = _file
        self.zawodnicy = []
        self.waga = []
        self.wzrost = []
        self.zb_kraje = set()
        self.sl_z = dict()
        self.sl_sr_wz = dict()
        self.lista_wz = []



    def prepare_data(self):
        read_csv = super().open_csv_file_read
        for row in read_csv:
            self.zawodnicy.append(row)
            self.waga.append(row[5])
            self.wzrost.append(row[4])
            self.zb_kraje.add(row[2])
            self.sl_z[row[2]] = self.sl_z.get(row[2], 0) + 1
            tmp_wz = [row[2], row[4]]
            self.lista_wz.append(tmp_wz)

    @property
    def waga(self):
        print(f'najlżejszy: {list(row[0] + " " + row[1] for row in self.zawodnicy if row[5] == min(self.waga))}')
        print(f'najcięższy: {list(row[0] + " " + row[1] for row in self.zawodnicy if row[5] == max(self.waga))}')
        print(f'najwyższy: {list(row[0] + " " + row[1] for row in self.zawodnicy if row[4] == max(self.wzrost))}')
        print(f'najniższy: {list(row[0] + " " + row[1] for row in self.zawodnicy if row[4] == min(self.wzrost))}')




# Pan Tadeusz
a = ReadTxtFiles('pan-tadeusz.txt', 'Tadeusz', txt_openmode='read')
print(a.word_counter())

b = ReadTxtFiles('pan-tadeusz.txt', txt_openmode='readlines')
for word, count in sorted(b.all_words_counter.items(), key=lambda item: item[1], reverse=True):
    print(f'{word} -> {count}')

#zawodnicy
c = ReadCsvFile('zawodnicy.csv')
c.prepare_data()
print(c.waga)



# # ## 6. Przetwarzanie plików
# # ​
# # ### Zadanie 6.1 | Dane skoczków narciarskich (3 godz.)
# # ​
# # Plik CSV z danymi: http://pgradzinski.students.alx.pl/kpython/zawodnicy.csv
# # ​
# # Korzystając z pliku CSV z danymi skoczków narciarskich napisz programy, które wczytują ten plik i:
# # ​
# # 1. wypisuje najwyższego, najwyższego, najcięższego i najlżejszego skoczka;
# # gdyby kilku miało taką samą wagę lub wzrost, to wystarczy wypisać jednego z nich.
# # 2. liczy ile łącznie ważą reprezentanci Polski (np. żeby sprawdzić czy zmieszczą się w windzie na skocznię ;)).
# # Pozwól użytkownikowi podać kraj (niekoniecznie musi być Polska).
# # 3. (trudniejsze) dla wszystkich krajów oblicza ilu jest zawodników z tego kraju; tzn. ma się wypisać,
# # być może w innej kolejności:
#
#
# #
# import csv
#
#
# with open('zawodnicy.csv', 'r', newline='', encoding="utf8") as plik_csv:
#     read_csv = csv.reader(plik_csv, delimiter=';')
#     zawodnicy = []
#     waga = []
#     wzrost = []
#     zb_kraje = set()
#     sl_z = dict()
#     sl_sr_wz = dict()
#     lista_wz = []
#     for row in read_csv:
#         zawodnicy.append(row)
#         waga.append(row[5])
#         wzrost.append(row[4])
#         zb_kraje.add(row[2])
#         sl_z[row[2]] = sl_z.get(row[2], 0) + 1
#         tmp_wz = [row[2], row[4]]
#         lista_wz.append(tmp_wz)
# # 1
# print(f'najlżejszy: {list(row[0] + " " + row[1] for row in zawodnicy if row[5] == min(waga))}')
# print(f'najcięższy: {list(row[0] + " " + row[1] for row in zawodnicy if row[5] == max(waga))}')
# print(f'najwyższy: {list(row[0] + " " + row[1] for row in zawodnicy if row[4] == max(wzrost))}')
# print(f'najniższy: {list(row[0] + " " + row[1] for row in zawodnicy if row[4] == min(wzrost))}')
#
# # 2
# kraj_z = input(f'podaj kraj: {zb_kraje}:')
# print(f'waga wszystkich {kraj_z}: {sum(list(int(row[5]) for row in zawodnicy if row[2] == kraj_z))}')
#
# # 3
# for _kraj, liczba in sorted(sl_z.items(), key=lambda item: item[1], reverse=True):
#     print(f'{_kraj} - {liczba}')
#
# # 4
# for kraj in zb_kraje:
#     print(kraj, '-',
#           len((list(filter(lambda item: item[0] == kraj, lista_wz)))), '-',
#           f'{sum(int(t[1]) for t in lista_wz if t[0] == kraj) / len((list(filter(lambda item: item[0] == kraj, lista_wz)))):.2f}')
#
