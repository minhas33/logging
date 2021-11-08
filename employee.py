import logging

logging.basicConfig(filename='employee.log', level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s', filemode='w')

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        logging.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Minhas', 'Iqbal')
emp_2 = Employee('Muhammad', 'Safwan')