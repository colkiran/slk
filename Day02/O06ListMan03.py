
# function that can add  values into a list - append, extend and insert

print("{:-^40}".format("append"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.append(6)
l1.append(7)
l1.append(8)
l1.append(9)
print(f"l1 :{l1}")
l1.append([10, 11, 12, 13, 14])
print(f"l1 :{l1}")
print(l1[9][1:4])

print("Extend".center(40, "-"))
l2 = [1, 2, 3, 4, 5]
print(f"l2 :{l2}")

l2.extend([6, 7])
l2.extend([8,9])
print(f"l2 :{l2}")

print("insert".center(40, "-"))
l3 = [1, 2, 3, 4, 5,]
print(f"l3 :{l3}")

l3.insert(1, 1.5)
l3.insert(3, 2.5)
l3.insert(5, 3.5)
l3.insert(7, 4.5)

print(f"l3 :{l3}")
