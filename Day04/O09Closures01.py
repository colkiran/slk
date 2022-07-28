
# closure
def outerFun(name):
    gname = f"Mr. {name}"

    def innerFun():
        print(f"Greetings {gname}")
        print(name)

    innerFun()

outerFun("Rahul")

