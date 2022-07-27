
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 40)
d2 = {'name': 'Sachin', 'runs': 135, 'oppn': 'West Indies', 'venue': 'Sabina Park'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 40)
d3 = dict([('name', 'rahul'), ('runs', 140), ('oppn', 'south Africa'), ('venue', 'Kingsmeed')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 40)
d4 = dict(name="Sourav", runs=185, oppn='sri lanka', venue="lords")
print(f"d4 :{d4}")
print(type(d4))

print("-" * 40)
player = {'name': 'Rahul', 'runs': 90, 'oppn': 'Australia', "venue": 'Perth'}
print(f"player :{player}")

# read
print("-" * 40)
print(player['runs'])
print(player['oppn'])

print("-" * 40)
for i in player:
    print(i)

# update
print(f"player")
player['age'] = 34
player['year'] = 2005
print(f"player :{player}")

# delete
del  player['oppn']
del  player['venue']
print(f"player :{player}")

print("-" * 40)
print(f"player :{player}")
player['runs'] = 150
player['age'] = 32
print(f"player :{player}")

print("-" * 40)
# print(player['oppn'])
print(player.get('oppn', "Invalid Key, Please enter a valid key"))
print(player.get('name', "Invalid Key, Please enter a valid key"))

print("-" * 40)
print(dir(player))

