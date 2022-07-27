
# copy, sort, reverse

print("copy".center(40, "-"))
l1 = list(range(1, 6))
print(f"l1 Before :{l1}")
l2 = l1                    # Shallow copy - copies the address
print(f"l2 Before :{l2}")

l2.extend([6, 7, 8, 9])
print(f"l2 After :{l2}")
print(f"l1 After :{l1}")

print("-" * 40)
l3 = list(range(6, 11))
print(f"l3 Before :{l3}")
l4 = l3.copy()                  # deep copy - copies only the data
print(f"l4 before  :{l4}")

l4.append(11)
l4.append(12)
l4.append(13)
print(f"l4 after :{l4}")
print(f"l3 after :{l3}")

print("-" * 40)
l5 = [11, 22, 33, 44, [2, 4, 6, 8, 10], 55]
print(f"l5 Before :{l5}")
l6 = l5.copy()
print(f"l6  Before :{l6}")

l6[4].append(12)
l6[4].append(14)
l6[4].append(16)

print(f"l6 After :{l6}")
print(f"l5 After :{l5}")

print("-" * 40)
l7 = [1, 2, 3, 4, 5, ['a', 'b', 'c']]
print(f"l7 Before :{l7}")
from copy import deepcopy
l8 = deepcopy(l7)
print(f"l8 Before :{l8}")

l8[5].append('d')
l8[5].append('e')
print(f"l8 After :{l8}")
print(f"l7 After :{l7}")

print("Sort".center(40, "-"))
# sort , sorted (sort will sort the original list, sorted will return a copy of the sorted list)
l1 = [10, 5, 7, 1, 9, 2, 8, 4, 6, 3]
print(f"l1 :{l1}")
resAsc = sorted(l1)
print(f"Ascending :{resAsc}")
resDesc = sorted(l1, reverse=True)
print(f"Descending :{resDesc}")

print('-' * 40)
l1 = [10, 'zebra', 'apple', 5,'yellow', 'blue', 7, 'pink', 'green', 1, 'cat', 'queen', 9, 'red',
      'green',2, 'white', 'mango', 8, 'turtle', 'dog', 4, 6, 3, 19, 145, 1234, 24, 2018, 275]
print(f"l1 :{l1}")
print("-" * 40)
res = sorted(l1, key=ascii)
print(f"res :{res}")

cities = ['thiruvananthapuram', 'bangalore', 'chennai', 'delhi', 'kanyakumari', 'pune',
          'mumbai', 'hyderabad', 'vishakapatnam', 'mysore', 'ooty']
print(f"cities :{cities}")
res  = sorted(cities, key=len)
print(f"res :{res}")

print("reversed".center(40, "-"))
l1 = [10, 5, 7, 1, 9, 2, 8, 4, 6, 3]
print(f"l1 :{l1}")
l1.reverse()
print(f'l1 :{l1}')