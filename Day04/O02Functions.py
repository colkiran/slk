
def greet():
    print("Welcome Mr. Sachin Tendulkar to the event.....")

def greetGst(gname):
    print(f"Welcome Mr. {gname} to the event......")

# city as default argument and gname as non default argument
def greetGstCty(gname, city="Mumbai"):
    print(f"Welcome Mr. {gname} from {city} to the event......")

greet()
greetGst("Rahul")
greetGstCty("Sachin")
greetGstCty("Sunil")
greetGstCty("Rahul", "Bangalore")           # overriding the value of city

print("-" * 40)
# Named Arguments
def adnission(name, dob, qlf, conno, adr, plc, idprf):
    print(f'Name :{name}')
    print(f"DOB :{dob}")
    print(f"Qualification :{qlf}")
    print(f"Contact No. :{conno}")
    print(f"Address :{adr}")
    print(f"Place :{plc}")
    print(f"ID proof :{idprf}")

adnission(plc="Chennai", conno=9349593459, dob="09/10/1989", name="Kenith", idprf= "Adhar card",
          adr='10th cross, Anna nagar', qlf='MBA')

print("-" * 40)
# Variable Length Arguments

def MultiplyMe(*numbers):
    print(numbers)
    print(*numbers)
    prod = 1
    for number in numbers:
        prod *= number
    return prod

res = MultiplyMe(1, 2, 3, 4, 5)
print(f"res :{res}")

print("-" * 40)
# arguments like dictionary syntax

def extractAll(**details):
    print(details)
    for k, v in details.items():
        print(k, "=>", v)

extractAll(name="Virat", runs=165, oppn="Australia", venue="Gabba")

print("-" * 40)
# return values from a function
def MultiplyMe(x, y):
    return x * y

print(f'The product of 10 and 50 is :{MultiplyMe(10, 50)}')

# recursive calls
# function calling itself
def fact(num):
    if num <= 1:
        return 1
    else:
        return num * fact(num - 1)

n = int(input("Enter a number :"))
print(f"The factorial of {n} is {fact(n)}")

print("-" * 40)
# fibanocci series
# 0, 1, 1, 2, 3, 5, 8, 13,
def recur_fib(n):
    if n <= 1:
        return n
    else:
        return recur_fib(n-1) + recur_fib(n-2)

nterms = int(input("Enter a positive number :"))
print("Fibanocci Sequence")
for i in range(nterms):
    print(recur_fib(i), end=" ")
print("")

# how many values can a function return
def ArithmeticCalc(x, y):
     sum = x + y
     diff = x - y
     prod = x * y
     quot = x / y
     return sum, diff, prod, quot

print(ArithmeticCalc(20, 8))

print("-" * 40)
print("-" * 40)
# Doc Strings
def fun():
    # this is a comment
    "This is a doc string"
    print("Hello World")

fun()
print(fun.__doc__)

print("-" * 40)
print("-" * 40)

def fun1(x, y):
    """
    Function- fun1(x, y)
    the function fun1 takes two arguments that is x and y, the data type of these arguments should be the same
    if integer
    -----------
    fun1(int, int)
    then the function fun1 will return the sum of these two numbers
    if strings
    fun1(str1, str2)
    then the function fun1 will return the concatenated string of str1 and str2
    """
    return  x + y

print(fun1(10, 30))
print(fun1("hello ", "World"))

print("-" * 40)
print("-" * 40)

help(fun1)