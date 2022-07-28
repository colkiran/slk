
def outerFun(greet):
    def innerFun(name):
        print(greet, name)
    return innerFun

outerFun("Greetings")("Sachin")
print("-" * 40)

# simple curry
hndGreet = outerFun("Namaskar")
tmlGreet = outerFun("Vannakam")
engGreet = outerFun("Welcome")

hndGreet("Sachin")
tmlGreet("Dhoni")
