'''with open("file.txt","w") as file:
    file.write("hello world")
with open("file.txt","r") as file:
    print(file.read())
with open("file.txt","a") as file:
    file.write("python programming")

# task1 
## keep asking valid integer number
## if not valid integer number, print error

while True:
    try:
        num = int(input("Enter a valid integer: "))
        print("You entered:", num)
        break
    except ValueError:
        print("Error: Please enter a valid integer.")'''

# task 2 
## handle index error while accessing list elements if it is out of range handle it
#l = [1,2,3,4,5,6,7,8,9,10]
#print(l[10])
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]

try:
    print(l[10])
except IndexError:
    print("Error: List index is out of range.")
