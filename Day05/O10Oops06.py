
class Player:
    team = "India"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is :{self.name}\nAge is :{self.age}")

    @classmethod
    def CreatePlayer(cls, fname, lname, age):
        print("Factory....")
        return cls(f"Mr. {fname} {lname}", age)

    @classmethod
    def CP_team(cls, tm):
        Player.team = tm

ply1 = Player("Rahul", 34)
ply1.get_details()
print("-" * 40)

ply2 = Player.CreatePlayer("Virat", "Kholi", 28)
ply2.get_details()
print("-" * 40)

Player.CP_team("CSK")
print(Player.team)
print(ply1.team)
print(ply2.team)