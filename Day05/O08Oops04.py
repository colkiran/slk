
class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    def __del__(self):
        print("=" * 40)
        print("Destructor called.....")
        print(f"{self.name} deleted...")

ply1 = Player("Sachin", 36)
ply1.get_details()

print("-" * 40)
ply2 = Player("Rahul", 34)
ply2.get_details()

print("-" * 40)
print(ply1.__dict__)
print(ply2.__dict__)
ply2.runs = 45
print(ply2.__dict__)
print(ply1.__dict__)
