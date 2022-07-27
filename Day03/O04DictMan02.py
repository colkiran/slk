
print("keys".center(40,"-"))
player = {'name': 'Messi', 'goals': 3, 'oppn': "real madrid", 'venue': 'Camp nou'}
print(f"player :{player}")
print("-" * 40)

k = player.keys()
print(f"k :{k}")
print(type(k))

for k in player.keys():
    print(k + "=>" + str(player[k]))

print("Values".center(40, "-"))
player = {'name': 'Messi', 'goals': 3, 'oppn': "real madrid", 'venue': 'Camp nou'}
print(f"player :{player}")
v = player.values()
print(f"v :{v}")

print("fromkeys".center(40, "-"))
cities = ['blr', 'che', 'mum', 'del','kol', 'hyd']
print(f"cities :{cities}")
print(type(list))

res1 = dict.fromkeys(cities)
print(f"res1 :{res1}")

res2 = dict.fromkeys(cities, 22)
print(f"res1 :{res2}")

print("setdefault".center(40, "-"))
# used to add new key value pair into the dictionary
emp = {'name': 'Kevin', 'age': 34, 'desig': 'BDM', 'dept': 'mkt'}
print(f"emp :{emp}")
emp.setdefault('dept', 'finance')
emp.setdefault("salary", 85000)
print(f"emp :{emp}")

print("pop".center(40, "-"))
player = {'name': 'Messi', 'goals': 3, 'oppn': "real madrid", 'venue': 'Camp nou'}
print(f"player :{player}")

res= player.pop('venue')
print(f"res :{res}")

print("popitem".center(40, "-"))
player = {'name': 'Messi', 'goals': 3, 'oppn': "real madrid", 'venue': 'Camp nou'}
print(f"player :{player}")

res = player.popitem()
print(f"res :{res}")
res = player.popitem()
print(f"res :{res}")
print(f"player :{player}")

print("items".center(40, "-"))
# combination of keys and values
emp = {
    'emp1' :{'name': 'Jack', 'age': 28, 'desig': 'TL', 'dept': "HR", 'sal': 45000},
    'emp2':{'name': 'Tina', 'age': 24, 'desig': 'SE', 'dept': "IT", 'sal': 65000},
    'emp3':{'name': 'Mike', 'age': 34, 'desig': 'MGR', 'dept': "Finance", 'sal': 75000}
}

print(f"emp :{emp}")
print("-" * 40)
print(f"emp1 :{emp['emp1']}")
print("-" * 40)
print(f"emp2 :{emp['emp2']}")
print("-" * 40)
print(f"emp3 :{emp['emp3']}")

print("-" * 40)
for ky, info in emp.items():
    print(ky)
    print("----")
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 40)
