
# emulate printf of C language
format = "Welcome %s, what a %s player"
print(f"format :{format}")
values = ("Sachin", "superb")                   # tuples
print(values)
print(format % values)
print("-" * 40)

format = "Welcome %s, your rating of %.3f, what a %s player"
print(format % ("Sachin", 4, "class"))
print(format % ("Sachin", 4.2, "class"))
print(format % ("Sachin", 4.2342546458, "class"))

print("Welcome %s, your rating of %.3f, what a %s player" % ("Sachin", 4, "class"))

print("-" * 40)
# emulate unix shell syntax
from string import Template
tmpl = Template("Welcome $name, what a $adj player")
print(tmpl)
res = tmpl.substitute(name= "Sachin", adj = "class")
print(f"res :{res}")

# format string of python
print("Welcome {}, what a {} player for {}".format("Sachin", "class", "India" ))
print("Welcome {0}, what a {1} player for {2}".format("Sachin", "class", "India"))
print("Welcome {1}, what a {2} player for {0}".format("India", "Sachin", "class"))

print("Welcome {name}, what a {adj} player for {ctry}".format(
    ctry="India", name="Sachin", adj="class"))

print("Welcome {name}, your rating of {rating}, what a player".format(
    name = "sachin", rating=4))

print("Welcome {name}, your rating of {rating:.3f}, what a player".format(
    name = "sachin", rating=4.2))

# interpolation
from math import pi, e
print(f"PI = {pi} and eulers constant = {e}")

print("PI = {} and eulers constant = {}".format(pi, e))
print("PI = {} and eulers constant = {} and magic_number = {}".format(pi, e, 40585))

print("-" * 40)
full_name = ["Sachin", "Tendulkar"]
print("Mr. {name}".format(name = full_name))
print("Mr. {name}".format(name = full_name[0]))
print("Mr. {name[0]} {name[1]}".format(name= full_name))

print("-" * 40)
import math
print(__name__)
print(math.__name__)

print("the {mod.__name__} module gives the value of pi={mod.pi} and eulers {mod.e}".format(mod=math))

print("Conversions".center(40, "-"))
print("{val}  {val}  {val}".format(val = "A"))
print("{val!s}  {val!r}  {val!a}".format(val = "A"))

print("The number {num} {num} {num}".format(num = 36))
print("The number {num} {num:f} {num:b}".format(num = 36))
print("The number {num:10} {num:f} {num:b}".format(num = 36))
print("The number {num:5} {num:f} {num:b}".format(num = 36))

# alignment
print("{num1:15}Tendulkar".format(num1=36))
print("{num1:15}Tendulkar".format(num1="Sachin"))
print("{}".format("Sachin Tendukkar"))
print("{:.6}".format("Sachin Tendulkar"))

print("-" * 40)
print("{num1:-<15}Tendulkar".format(num1="Sachin"))
print("{num1:*^15}Tendulkar".format(num1="Sachin"))
print("{num1:#>15}Tendulkar".format(num1="Sachin"))

print("{pi:10.2}".format(pi = pi))
print("{pi:10.3}".format(pi = pi))
print("{pi:10.4}".format(pi = pi))
print("{pi:10.5}".format(pi = pi))

print("{pi:010.2}".format(pi = pi))
print("Hello World".center(40, "-"))
print("{:-^40}".format("Hello World"))