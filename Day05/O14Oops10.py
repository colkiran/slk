
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['C++', 'Java', 'J2ee', 'Spring', 'Hibernate', 'AngularJS']

    def __str__(self):
        return f"Name is :{self.name}\nSalary is :{self.salary}"

    def __len__(self):
        return len(self.tech)

    def __iter__(self):
        return iter(self.tech)

emp1 = Employee("Micheal", 45000)
print(emp1)

print(len(emp1))
print([t for t in emp1])               # List comprehension

