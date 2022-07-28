
def outerFun(greet):

    def innerFun(sep):

        def innerMost(name):
            import emojis
            emojized = emojis.encode(greet + " :" + sep + ": " + name)
            print(emojized)

        return innerMost
    return innerFun

KanGreet = outerFun("Namaskara")
KanGrtTgr = KanGreet("tiger")
KanGrtTgr("Prabhakar")




"""
outerFun("Welcome")("===>>")("Sachin")

engGreet = outerFun("Welcome")
engSngArw = engGreet("----->")

engSngArw("Messi")
"""