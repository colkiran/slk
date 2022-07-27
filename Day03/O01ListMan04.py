
# pop, remove, clear

print("pop".center(40, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

res = l1.pop(3)
print(f"res :{res}")
res = l1.pop(5)
print(f"res :{res}")
res = l1.pop(7)
print(f"res :{res}")
res = l1.pop()                  # no index then the last element of the list will be removed
print(f"res :{res}")

# res = l1.pop(7)
# print(f"res :{res}")

print(f"l1 :{l1}")

print("{:-^40}".format("remove"))
l2 = [1, 2, 3, 1, 2, 1, 1, 1, 2, 2, 2, 1, 2, 2, 1, 2, 3, 1, 2, 2, 1, 2, 1, 3, 1, 2, 1]
print(f"l2 :{l2}")

l2.remove(1)
l2.remove(3)
# l2.remove(4)
print(f"l2 :{l2}")

print("-" * 40)
l2 = [1, 2, 3, 1, 2,3, 1, 2, 3, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1 , 2, 3, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1]

# for i in l2:
#     if i == 1:
#         l2.remove(1)

# while(l2.count(1)):
#     l2.remove(1)

while True:
    try:
        l2.remove(1)
    except ValueError:
        break

print(f"l2 :{l2}")

print("clear".center(40, "-"))
l1 = list(range(1, 6))
print(f"l1 before :{l1}")
l1.clear()
print(f"l1 after :{l1}")

print("Count".center(40, "-"))
l2 = [1, 2, 3, 1, 2,3, 1, 2, 3, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1 , 2, 3, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1]

print(f"1 :{l2.count(1)}")
print(f"2 :{l2.count(2)}")
print(f"3 :{l2.count(3)}")

print("index".center(40, "-"))
l3 = [1, 2, 3, 1,  1,1, 1, 1, 1, 2, 3,2, 1, 2, 1, 3, 1,1, 1, 3]
print(f"l3 :{l3}")
print(f"3 :{l3.index(3)}")
print(f"3 :{l3.index(3, l3.index(3)+1)}")
print(f"3 :{l3.index(3, l3.index(3, l3.index(3)+1)+1)}")

