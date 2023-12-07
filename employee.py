"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name


class MonthlyEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def get_pay(self):
        return self.salary

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.get_pay()}."


class ContractEmployee(Employee):
    def __init__(self, name, hours_worked, hourly_rate):
        super().__init__(name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def get_pay(self):
        return self.hours_worked * self.hourly_rate

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour. Their total pay is {self.get_pay()}."


class CommissionEmployee(Employee):
    def __init__(self, name, base_salary, commission_rate, num_contracts):
        super().__init__(name)
        self.base_salary = base_salary
        self.commission_rate = commission_rate
        self.num_contracts = num_contracts

    def get_pay(self):
        commission = self.commission_rate * self.num_contracts
        return self.base_salary + commission

    def __str__(self):
        commission_str = f" and receives a commission for {self.num_contracts} contract(s) at {self.commission_rate}/contract"
        return f"{self.name} works on a monthly salary of {self.base_salary}{commission_str}. Their total pay is {self.get_pay()}."


# Create employee objects
billie = MonthlyEmployee('Billie', 4000)
charlie = ContractEmployee('Charlie', 100, 25)
renee = CommissionEmployee('Renee', 3000, 200, 4)
jan = CommissionEmployee('Jan', 25, 220, 3)
robbie = MonthlyEmployee('Robbie', 2000)
ariel = ContractEmployee('Ariel', 120, 30)

# Test the calculations and output
print(billie.get_pay())  # 4000
print(str(billie))  # "Billie works on a monthly salary of 4000. Their total pay is 4000."

print(charlie.get_pay())  # 2500
print(str(charlie))  # "Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500."

print(renee.get_pay())  # 3800
print(str(renee))  # "Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract. Their total pay is 3800."

print(jan.get_pay())  # 4410
print(str(jan))  # "Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410."

print(robbie.get_pay())  # 3500
print(str(robbie))  # "Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is 3500."

print(ariel.get_pay())  # 3600
print(str(ariel))  # "Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. Their total pay is 4200."