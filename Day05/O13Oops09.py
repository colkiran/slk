
class Emp:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is :{self.name}\nSalary is :{self.salary}"

    def __add__(self, other):
        return self.salary + other.salary

    def __sub__(self, other):
        return self.salary - other.salary

    def __mul__(self, other):
        return self.salary * other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __floordiv__(self, other):
        return self.salary // other.salary

emp1 = Emp("David", 15000)
emp2 = Emp("Kevin", 18000)

print(emp1 + emp2)
print(emp1 - emp2)
print(emp1 * emp2)
print(emp1 / emp2)
print(emp1 // emp2)