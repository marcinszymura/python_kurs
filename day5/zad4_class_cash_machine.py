# >>> cash_machine = CashMachine()
# >>> cash_machine.is_available
# False
# >>> cash_machine.put_money([200, 100, 100, 50])
# >>> cash_machine.is_available()
# True
# >>> cash_machine.withdraw_money(150)
# [100, 50]


class CashMachine:
    def __init__(self):
        self.__money_box = []

    @property
    def is_available(self):
        if len(self.__money_box) == 0:
            return False
        else:
            return True

    def update_cash_machine(self):
        list_of_denominations = []
        while False:
            x = input(int('kwota do wpłaty, 0 - koniec: '))
            if x == 0:
                True
            if x % 10 != 0:
                raise ValueError('zla wartość nominału')
            else:
                list_of_denominations.append(x)
        return list_of_denominations


    def put_money(self, list_of_denominations):

        list_of_denominations = [200, 100, 100, 50]
        self.__money_box = list_of_denominations
        return self.__money_box

    def withdraw_money(self, withdraw_value):
        if withdraw_value % 10 != 0:
            raise ValueError(f'Bankomat nie jest w stanie wypłacić kwoty: {withdraw_value}')
        temp_list = []
        for i in sorted(self.__money_box):
            if sum(temp_list) + i <= withdraw_value:
                temp_list.append(i)
        if sum(temp_list) == withdraw_value:
            for i in temp_list:
                self.__money_box.remove(i)
            return temp_list
        return []


start = CashMachine.update_cash_machine(self=)



class TestCashMachine:
    def test_init(self):
        cash_machine = CashMachine()
        assert cash_machine
        assert cash_machine.is_available == False

    def test_put_money(self):
        cash_machine = CashMachine()
        cash_machine.put_money([200, 100, 100, 50])
        assert cash_machine.is_available is True

    def test_withdraw_money(self):
        cash_machine = CashMachine()
        cash_machine.put_money([200, 100, 100, 50])
        assert cash_machine.is_available is True
        assert cash_machine.withdraw_money(150) == [50, 100]
        assert cash_machine.withdraw_money(600) == []
