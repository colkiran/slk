
"""
1. arithmetic operator
2. comparison or relational operator
3. logical
4. Bitwise
5. Ternary
"""

print("Arithmetic".center(40, "-"))
print("Add :", 10 + 3)
print("Sub :", 10 - 3)
print("Div :", 10 / 3)
print("Mul :", 10 * 3)
print("Floor Div :", 10 // 3)
print("Modulus :", 10 % 3)
print("Power :", 10 ** 3)
print("-" * 40)

print("Augmentor".center(40, "-"))
# +,  +=, -=. /=, *=
x = 10
print(f"x :{x}")
x += 3
print(f"x :{x}")
print("-" * 40)
x //= 3
print(f"x :{x}")

print("Comparison".center(40, "-"))
# ==, >=, <= !=
a = 10
b = 20
print(a == b)
print(a >= b)
print(a <= b)
print(a != b)

print("Logical Operators".center(40, "-"))
# and or not
print(1 == 1 and 2 == 2)
print(1 == 2 and 2 == 2)
print("-" * 40)
print(1 == 1 or 1 == 2)
print(2 == 1 or 1 == 1)
print("-" * 40)
print(not(1 == 1 or 1 == 2))
print(not(2 == 1 or 1 == 1))

print("-" * 40)
print(f"a :{ord('a')}" )                # interger represntation of unicode characters
print(f"z :{ord('z')}")
print(f"z :{ord('A')}")
print(f"z :{ord('Z')}")

print("bitwise operators".center(40, "-"))
print(5 | 3)
print(5 & 3)
print(5 ^ 3)
print(5 << 1)
print(8 << 1)
print(5 << 2)
print(16 >> 1)
print(5 >> 1)

print(~0)
print(~5)
print(~0)

print("ternary".center(40, "-"))
age = 14
print("eligible" if age >= 18 else "not eligible")
