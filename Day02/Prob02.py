
n = 0
for i in range(150, 50, -1):
    cntr = 0
    for j in range(1, i+1):
        if i %  j == 0:
            cntr += 1
            if cntr > 2:
                break
    if cntr == 2:
        print(i, end = " ")
        n += 1
print()

print(f"There are {n} prime numbers between 150 and 50")