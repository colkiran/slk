
for i in range(1, 10):
    print(i, end=" ")
print("")
print("hello")

print("-" * 40)
for i in range(1, 25):
    # if i > 20:
    #     break
    if i % 2 == 0:
        continue            # skip the iteration
    print(i, end=" ")
else:
    print("\nCompleted the iteration......")

