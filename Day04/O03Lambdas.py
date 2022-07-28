
def AddMe(x, y):
    return x + y

a = AddMe
res = a(10, 20)
print(f"res :{res}")

b = lambda x, y: x + y
res = b(100, 200)
print(f"res :{res}")

# map, reduce and filter
def square(num):
    return num * num

l = list(range(1, 11))

res = list(map(square, l))
print(f"res :{res}")

res = list(map(lambda x: x ** 2, l))
print(f"res :{res}")

print("-" * 40)
print("-" * 40)

months = ['dec', 'apr', 'aug',  'jan', 'jul', 'oct', 'feb', 'sep', 'mar', 'may', 'jun', 'nov']
print(f"months :{months}")

from calendar import month_name
def SrtMnt(mon):
    l = []
    for m in list(month_name):
        l.append(m[0:3].lower())
    if mon in l:
        return l.index(mon)

res1 = sorted(months, key=SrtMnt)
print(f"res1 :{res1}")

res2 = sorted(months, key=SrtMnt, reverse=True)
print(f"res2 :{res2}")

print("*-" * 40)
res = sorted(months, key=list(map(lambda x: x.lower()[0:3], list(month_name))).index)
print(f"res :{res}")

print("-" * 40)
# filter
l = list(range(1, 25))
res = list(filter(lambda x: x % 3 == 0, l))
print(f"res :{res}")

print("-" * 40)
from functools import reduce
l = [3, 8, 6, 9, 11, 7, 10, 5]
print(f"l :{l}")
res = reduce(lambda x, y: x if x > y else y, l)
print(f"res :{res}")

res = reduce(lambda x, y: x + y, l)
print(f"res :{res}")
