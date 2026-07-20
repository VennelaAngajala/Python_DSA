'''print("vennela\nvennela1")
print(r"\tcurrent\new\floder")
# / is escape character
# write a program to find odd or even with function:
def check_number(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

# Example usage
check_number(7)

l=[1,2,3,4,5]
l.pop()
print(l)
dict={
    "name":"vennela",
    "gender":"female",
    "age":20,
    "courses":["python","java","datascience"]
}
dict["name"]="Vennela angajala"
dict.update({"courses":["python","java","ML"]})
print(dict)
print(dict["name"])
print(dict.get("name"))
print(dict.keys())
print(dict.values())
print(dict.items())

def count(*args):
    print(type(args))
#count(1,2,3,4,5)
def dicts(**kwargs):
    print(type(kwargs))
#dict(name="vennela",age=20,gender="female")
def default(gender,age,name="vennela"):
    print(name,age,gender)'''

#OOPS 
'''l=[1,2,3]
s="string"
len(l)
len(s)'''

# 4 pillars of OOPS
# Encapsulation:
# Abstraction
# Inheritance:
# Polymorphism

#take a string as input and
#print it back by removing the first and last character of the input string

'''x="vennela"
x=x[1:-1]
x=x[""-1]
print(x)


while True:
    print("hi")'''
#take a number as input and find the sum of numbers from 1 to that number

n=int(input("enter a value:"))
sum=0
for i in range(1,x+1):
    sum+=i
print(sum)
