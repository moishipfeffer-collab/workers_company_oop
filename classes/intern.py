from classes.employee import Employee

class Intern(Employee):
    def __init__(self, name, salery,mounths):
        if not 1 <= mounths <= 12:
            raise ValueError("months must be 1-12")
        super().__init__(name, salery)
        self.mounths = mounths

    def title(self):
        return "intern"