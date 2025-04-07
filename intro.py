
# modules

'''
only import 
power function from math module

'''
from math import pow
import datetime as dt

data = pow(2,3)
print(data)

current_date = dt.datetime.now()    
print(f"log_{current_date.date()}.txt")