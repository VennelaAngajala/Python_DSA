# errors
# Value Error - data type mismatch
# Type Error - operations on incompatible types
# Index Error - Index out of range
# Key Error - Key is not present
# Name Error - we didn't declared variable
# Zero Division Error - divided by zero
# ModuleNotFound Error - library is not present

'''x=int(input("enter a number:"))
y=int(input("enter a number:"))
print(x/y)

x=int(input("enter a number:"))
y=int(input("enter a number:"))
try:
    print(x/y)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
finally:
    

    for i in range(5):
        if i==4:
            break
            print(i)
    else:
        print("done") 

try:
    a=int(input("enter a number:"))
    print(a)
except ValueError as e:
    print(e)
else:
    print("done")

# to throw error
a=int(input("enter a number:"))
if a < 0:
    raise ValueError("number is negative")
else:
    print(a)
'''



