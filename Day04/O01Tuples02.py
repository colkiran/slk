
"""
collection - lib
namedtuple - class

"""
from collections import namedtuple

nmdTpl = namedtuple("Products", "prdid prodname type price")
prd = nmdTpl(prdid=1001, prodname='Dairy milk', type='choclate', price=175 )
print(prd)

print("- " * 40)
print(f"Product ID  :{prd.prdid}")
print(f"Product Name :{prd.prodname}")
print(f"Product Type :{prd.type}")
print(f"Price        :{prd.price}")

# prd.price = 185