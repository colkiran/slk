
emp1 = {'name': 'Jack', 'age': 28, 'desig': 'TL', 'dept': "HR"}
emp2 =  {'name': 'Tina', 'age': 24, 'desig': 'SE', 'sal': 65000}

print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")
print('-' * 40)
emp1.update(emp2)
print(f"emp1 :{emp1}")

# dict copy or deepcopy
d1 = {'a': 'apple','b':'ball', 'c':'cat'}
print(f"d1 Before :{d1}")
d2 = d1
print(f"d2 Before :{d2}")

print("-" * 40)
d2['d'] = 'duck'
d2['e'] = "egg"
print(f"d2 After :{d2}")
print(f"d1 After :{d1}")

print("-" * 40)
d3 = {1: 'a', 2: 'b', 3: 'c'}
print(f"d3 before :{d3}")
d4 = d3.copy()
print(f"d4 before :{d4}")

d4[4] = 'd'
d4[5] = 'e'
print(f"d4 after :{d4}")
print(f"d3 after :{d3}")

print("-" * 40)
d5 = {1 :'aa', 2: 'bb', 3: {1: 10, 2: 20}, 4: 'cc', 5 :'dd'}
print(f"d5 before :{d5}0")
d6 = d5.copy()
print(f"d6 before :{d6}")

d6[3][3] = 30
d6[3][4] = 40
print(F"d5 After :{d5}")
print(f"d6 After :{d6}")

print("-" * 40)
d7 = {'name': "Micheal", 'age':30, 'gender' :'male', 'dept': 'IT', 'marks': {'Xth' : '78%', 'XIIth':'85%', 'degree' :'70%'}}
print(f"d7 :{d7}")
from copy import  deepcopy
d8 = deepcopy(d7)
print(f"d8 :{d8}")

d8['marks']['pg'] = '86%'
print(f"d8 After :{d8}")
print(f"d7 After :{d7}")