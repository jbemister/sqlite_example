class Employee:
    """class for storing employee data"""

    def __init__(self, employee_id, first, last, department_id, manager_id, pay):
        self.employee_id = employee_id
        self.first = first
        self.last = last
        self.department_id = department_id
        self.manager_id = manager_id
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Employee('{}', '{}', '{}', '{}', '{}')".format(self.first, \
            self.last, self.department_id, self.manager_id, self.pay)
