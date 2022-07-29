

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

    def append(self, val):
        self.tech.append(val)

    def __getitem__(self, index):
        return self.tech[index]

    def __setitem__(self, index, value):
        self.tech[index] = value

emp1 = Employee("Micheal", 45000)
print(emp1)

print(len(emp1))
print([t for t in emp1])               # List comprehension

print("-" * 40)
emp1.append("Python")
print([t for t in emp1])

print("-" * 40)
t = emp1[3]
print(f"t :{t}")

print("-" * 40)
emp1[3] = "ReactJS"
print([t for t in emp1])