class Employee:
    def __init__(self, firstname, lastname, rate_per_hour):
        self.registered_time = 0
        self.firstname = firstname
        self.lastname = lastname
        self.rate_per_hour = rate_per_hour


    def pay_salary(self):
        if self.registered_time <= 8:
            to_pay = self.registered_time * self.rate_per_hour
        else:
            to_pay = self.rate_per_hour * 8 + self.rate_per_hour * (self.registered_time - 8) * 2
        self.registered_time = 0
        return to_pay

    def register_time(self, hours):
        self.registered_time = hours


class PremiumEmployee(Employee):
    def __init__(self,firstname, lastname, rate_per_hour):
        super(PremiumEmployee, self).__init__(firstname, lastname, rate_per_hour)
        self.bonus = 0

    def give_bonus(self, amount):
        self.bonus += amount

    def pay_salary(self):
        to_pay = super().pay_salary()
        to_pay += self.bonus
        self.bonus = 0
        return to_pay


class TestEmployee:
    def test_init(self):
        employee = Employee('Jan', 'Nowak', 100.0)
        assert employee # czy nie none lub false
        assert employee.firstname == 'Jan'
        assert employee.lastname == 'Nowak'
        assert employee.rate_per_hour == 100.0

    def test_register_time(self):
        employee = Employee('Jan', 'Nowak', 100.0)
        employee.register_time(5)
        assert employee.registered_time == 5

    def test_pay_salary(self):
        employee = Employee('Jan', 'Nowak', 100.0)
        employee.register_time(5)
        assert employee.pay_salary() == 500
        assert employee.pay_salary() == 0

    def test_pay_salary_overhours(self):
        employee = Employee('Jan', 'Nowak', 100.0)
        employee.register_time(10)
        assert employee.pay_salary() == 1200
        assert employee.pay_salary() == 0

class TestPremiumEmployee:
    def test_give_bonus(self):
        employee = PremiumEmployee('Jan', 'Nowak', 100.0)
        employee.register_time(8)
        employee.give_bonus(1000)
        # assert employee.give_bonus(1200) == 1200
        assert employee.pay_salary() == 1800

