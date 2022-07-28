
fruits = [
    ('apple', 285),
    ('orange', 145),
    ('grapes', 120),
    ('gauva', 85),
    ('banana', 75),
    ('pine', 90),
    ('strawberry', 350),
    ('watermelon', 70)
]

print(f"Fruits :{fruits}")
print("-" * 40)

print(["fruit" for fruit in fruits])
print("-" * 40)

print([fruit for fruit in fruits])
print("-" * 40)

print([fruit[0] for fruit in fruits])
print("-" * 40)

print([fruit[1] for fruit in fruits])
print("-" * 40)

print([fruit[1] * 0.9 for fruit in fruits])
print("-" * 40)

print([fruit[1] * 0.75 for fruit in fruits])
print("-" * 40)

print([(fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75) for fruit in fruits])
print("-" * 40)

res = [(fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75) for fruit in fruits
       if fruit[1] > 100 ]
print(f"res :{res}")
