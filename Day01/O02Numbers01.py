
"""
1nt
float
complex
"""

a = 10
b = -10
print(f"a :{a}")
print(type(a))              # RTTI - runtime type identification
print(f"b :{b}")
print(type(b))

c = 4.5
d =-4.5
print(f"c :{c}")
print(type(c))
print(f"d :{d}")
print(type(d))

e = +2e3
f = -2e3
print(f"e :{e}")
print(type(e))
print(f"f :{f}")
print(type(f))

g = 3.14j
h = -3.14j
print(f"g :{g}")
print(type(g))
print(f"h : {h}")
print(type(h))

print("-" * 40)
x = 2 + 3.5
print(f"x :{x}")
print(type(x))

print("-" * 40)
x = 2
y = 3.5
i = 3.5
z = x + y
j = y + i
print(type(x))
print(type(y))
print(type(i))
print(type(z))
print(type(j))

print("conversion".center(40, "-"))
x = 100
print(f"{type(x)}\t\t{x}")
print(f"{type(float(x))}\t\t{float(x)}")
print(f"{type(complex(x))}\t\t{complex(x)}")
print(f"{type(bool(x))}\t\t{bool(x)}")

print("Number System".center(40, "-"))
print(11)           # decimal number
print(0b11)         # binary
print(0b101)        # binary
print(0o11)         # octal
print(0o101)        # octal
print(0xe)          # hexa
print(0xa)          # hexa

print("Number System conversion".center(50, "-"))
a  = 100
print(bin(a))
print(oct(a))
print(hex(a))
