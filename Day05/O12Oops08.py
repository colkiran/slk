
class Player:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is :{self.name}\nSalary is :{self.salary}"

    def __gt__(self, other):
        return self.salary > other.salary

    def  __eq__(self, other):
        return self.salary == other.salary

ply1 = Player("Jack", 50000)
print(ply1)

print("-" * 40)
ply2 = Player("Jill", 50000)
print(ply2)

print("-" * 40)
if ply1 > ply2:
    print("{} salary of {} is greater than {} salary {}".format(ply1.name,
                                                ply1.salary, ply2.name, ply2.salary))
else:
    print("{} salary of {} is greater than {} salary {}".format(ply2.name,
                                                                ply2.salary, ply1.name, ply1.salary))

print("-" * 40)
if ply1 == ply2:
    print("{} salary of {} is  equal to {} salary of {} ".format(ply1.name, ply1.salary, ply2.name,
                                                                ply2.salary))
else:
    print("{} salary of {} is Not equal to {} salary of {} ".format(ply2.name, ply2.salary, ply1.name,
                                                                ply1.salary))