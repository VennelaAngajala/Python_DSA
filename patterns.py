'''n=5
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
# right angled triangle
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()


n=5
for i in range(n,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()

#diamond pattern


# Upper half
n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()

# Lower half
for i in range(n - 2, -1, -1):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()

# first how many rows
# second how many spaces
# third how many stars


# Armstrong Number
#153 = 1^3 + 5^3 + 3^3

n=int(input("enter a number:"))
sum = 0
length=len(str(n))
temp = n
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if n==sum:
    print(n,"is an armstrong number")
else:
    print(n,"is not an armstrong number")

#Hollow Square Pattern

n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''

# Pascals Patterns

n = 5

for i in range(n):
    num = 1

    print(" " * (n - i), end="")

    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)

    print()