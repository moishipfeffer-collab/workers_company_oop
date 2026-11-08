from classes.employee import Employee

class Manager(Employee):
    def __init__(self, name, salery,bonus):
        super().__init__(name, salery)
        self.bonus = bonus

    def title(self):
        return "manager"
    
    @property
    def monthly_cost(self):
        return super().monthly_cost + self.bonus
