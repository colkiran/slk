
def timeCalc(fnc):
    def helper(m):
        from datetime import datetime
        st = datetime.now()
        fnc(m)
        et = datetime.now()
        print(f"The total time taken by {fnc.__name__} is {et -st}")
    return helper

@timeCalc
def Test(max):
    l = []
    for i in range(1, max+1):
        for j in range(1, i + 1):
            l.append(i ** 3)

Test(5000)

print("-" * 40)
def fun(*args, **kwargs):
    print(args)
    print(kwargs)

fun(10, 20, 30, 40, 50, name='sachin', age=36, runs=45000, matches=560)

