
def funLogger(fnc):
    def helper():
        print("My info logged into the service...")
        fnc()
        print("My info logger channel closed....")
    return helper

def normalfun():
    print("I should be called Normal.......")

print("-" * 40)
funLogger(normalfun)                #no output
print("-" * 40)
funLogger(normalfun)()
print("-" * 40)
res_fun = funLogger(normalfun)
res_fun()
print("-" * 40)
print("-" * 40)
normalfun = funLogger(normalfun)
normalfun()

print("-" * 40)
print("-" * 40)
print("-" * 40)

@funLogger                  # decorator
def BasicFun():
    print("I should be called basic.....")

BasicFun()
