# python OOP - Classes!

class Employe():
    def __init__(self, first , last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + '@company.com'

    def full_name(self):

        return '{} {}'.format(self.first,self.last)


emp_1 = Employe('Muhammad','Wasim',50000)
emp_2 = Employe('first_name' ,'last_name',40000)

#print(emp_1.email)
#print(emp_2.email)
'''
emp_1.first = 'Muhammad'
emp_1.last = 'Wasim'
emp_1.pay = 50000

emp_2.first = 'first_name'
emp_2.last = 'last_name'
emp_2.pay = 40000

print(emp_1.first + ' ' + emp_1.last)

'''

print(emp_1.full_name())
print(emp_2.full_name())

print(Employe.full_name(emp_1))