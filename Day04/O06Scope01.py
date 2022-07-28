"""
1. global
2. local
3. non local

accessibility of a variable  - print the value, but cannot change the value
"""

glbX = 100

def fun(a):                     # local variable
    global glbX                   # do not assign any value in this line
    print(f"a :{a}")
    glbX = 500
    print(f"inside glbX :{glbX}")
    y = "Hello"
    print(f"y :{y}")            # local variable

print(f"Before glbX = {glbX}")
fun(10)
print(f"After glbX = {glbX}")
