
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 40)
l2 = [1, 2, 3, 4, 5.1, 6.4, 7.1, 'eight', 'nine', 'ten', 11+0j, 12-4j, True, False]
print(f"l2 :{l2}")
print(type(l2))
print(id(l2[0]))
print(id(l2[1]))
print(id(l2[2]))
print(id(l2[3]))
print(id(l2[4]))

print("-" * 40)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 40)
l4 = [1, 2, 3, 4, 5]
print(f"l4[2] :{l4[2]}")
for i in l4:
    print(i, end=" ")
print()

print("-" * 40)
l4[4] = 44                  # insert a new element
print(f"l4 :{l4}")

print("-" * 40)
del l4[3]
print(f"l4 :{l4}")

# unpack a list
print("-" * 40)
values = list(range(10, 40, 10))
print(f"values :{values}")
a, b, c = values
print(a, b, c, sep=", ")

values = list(range(10, 101, 10))
print(f"values :{values}")

a, b, *c = values
print(a, b, c, sep=", ")
print("-" * 40)

a, *b, c = values
print(a, b, c, sep=", ")
print("-" * 40)

*a, b, c = values
print(a, b, c, sep=", ")
print("-" * 40)

list1 = [1, 2, 3, 4, 5]
list2 = [11, 12, 13, 14, 15]

print(f"list1 :{list1}")
print(f"list2 :{list2}")

list3 = [list1, list2]
print(f"list3 :{list3}")
print("-" * 40)

list4 = [*list1, *list2]                    # unpack
print(f"list4 :{list4}")

print("list3 :", len(list3))
print("list4 :", len(list4))
print("-" * 40)
print(f"list1 :{list1}")
print(f"unpack :", *list1)
