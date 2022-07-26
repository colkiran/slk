
st = "hello world"
st1 = "the quick brown fox the jumps over the lazy dog"

print("find".center(40, "-"))
print(f"st :{st}")
print(st.find("l"))
print(st.find("l", 4))

print(st1.find("the"))
print(st1.find("the", 4))

print("replace".center(40, "-"))
print(f"st :{st}")
print(st.replace("h", "H"))

res = st.replace("l", "L", 2)
print(f"res :{res}")

print("-" * 40)
res = st1.replace("the", "The", 1)
print(f"res :{res}")

print("-" * 40)
print(st1[0:st1.find("r", 12)+1] + st1[st1.find("r", 12)+1:].replace("the", "The"))

a =  st1[:st1.find("the", st1.find('the')+1)]
b = st1[st1.find("the", st1.find('the')+1):].replace("the", "The", 1)

print(a)
print(b)

print("-" * 40)
st = "***********Hello World************"
print(f"st :{st}")

res = st.lstrip("*")
print(f"res :{res}")

res = st.rstrip("*")
print(f"res :{res}")

res = st.strip("*")
print(f"res :{res}")

