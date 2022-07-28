
# nested functions
def outerFun(name):            # local
    gname = f"Mr. {name}"      # local

    def innerFun():
        nonlocal gname              # only local variables can be converted to nonlocal
        gname = "Mr. Rahul"
        print(f"Greetings {gname}")

    innerFun()
    print(f"After :{gname}")

outerFun("Sachin")

os.system("cls")
