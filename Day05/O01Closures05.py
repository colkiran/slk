
def sum(*args):
    print("sum called......")
    add = 0
    for arg in args:
        add += arg
    return add

def diff(x, y):
    print("diff called.....")
    return x - y

def log_details(fnc):                   # HOF
    loginfo = "Logging about done...."

    def innerFun(*args):
        print(loginfo)
        print(fnc(*args))
        print("-" * 40)

    return innerFun

sumLgr = log_details(sum)
diffLgr = log_details(diff)

sumLgr(35, 85)
diffLgr(90, 45)

print("-" * 40)
sumLgr(10, 20, 30, 40, 50, 60)
sumLgr(10, 20, 30, 40)
sumLgr(10, 20)
