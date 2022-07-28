
# closure
def outerFun(name):                         # HOF - Higher Order Function
    gname = f"Mr. {name}"

    def innerFun():
        print(f"Greetings {gname}")
        print(name)

    return innerFun

outerFun("Rahul")()
print("-" * 40)

print(outerFun.__name__)
print(outerFun("hello").__name__)

print("-" * 40)
infun = outerFun("Sachin")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("-" * 40)
infun()                         # calls the inner function
