
letters = ['a', 'b', 'c', 'd', 'e']
print(f"letters :{letters}")

print("-" * 40)
for letter in letters:
    print(letter, end=" ")
print()

print("-" * 40)
for letter in enumerate(letters):
    print(letter, " ", end=" ")
print()
print("-" * 40)

for letter in enumerate(letters):
    print(letter[0], letter[1])

print("-" * 40)

for index, letter in enumerate(letters):
    print(index, letter)

print("-" * 40)
my_list = [[1, 2, 3, 4], [6, 7, 8, 9], [11, 12, 13, 14]]
print(f"mylist :{my_list}")

for lst in my_list:
    print(lst)
print("-" * 40)

for idx, lst in enumerate(my_list):
    print(f"{idx}\t{lst}")
print("-" * 40)

for idx, lst in enumerate(my_list):
    print(f"List{idx}")
    for ind, num in enumerate(lst):
        print(f"\t{ind}\t{num}")

print("-" * 40)
print(dir(my_list))
