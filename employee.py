class Employee:
    """class for storing employee data"""

    def __init__(self, first, last, department_id, manager_id, pay):
        self.first = first
        self.last = last
        self.department_id = department_id
        self.manager_id = manager_id
        self.pay = pay

    @classmethod
    def prompt_to_create(cls):
        """ this class method is intended to be used exclusively with the
            sqlite.py file in the same directory.
        -param cls: the Employee class
        -return: Either a new class instance or the raw input if instance
                 creation fails
        """
        print("\nInput new employee information or 'q' to quit.\n")
        r_input = input("Format as follows:\n"
                        "first,last,department_id,manager_id,pay\n\n")
        new_class = r_input.split(',')
        try:
            return cls(new_class[0], new_class[1], new_class[2],
                       new_class[3], new_class[4])
        except:
            return r_input

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Employee('{}', '{}', '{}', '{}', '{}')".format(self.first, \
            self.last, self.department_id, self.manager_id, self.pay)
