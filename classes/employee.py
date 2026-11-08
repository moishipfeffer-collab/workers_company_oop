class Employee:
    def __init__(self,name,salery):
        self.name = name
        self.salery = salery

    def title(self):
        return "employee"
    
    @property
    def monthly_cost(self):
        return self.salery
    
    @property
    def describe(self):
        return f"name: {self.name} ({self.title()}): {self.monthly_cost}"
      
    



