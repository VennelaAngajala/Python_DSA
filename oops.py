# 4 pillers of OOPS
# Encapsulation
'''class A:
    def __init__(self,name,age,gender):#constructor
        self. name=name #private variable can be accessed inside of same class which defines with __
        self. age=age # protected variable can be accessed inside of same class and its child class  which defines with __
        self. gender=gender # public variable can be accessed inside of same class and outside of all classes which defines with no prefix

a1=A("vennela",20,"female")
a2=A("Ashu",21,"female")
print(a1.name)
print(a2.age)
print(a2.gender)
# Abstraction
from abc import ABC,abstractmethod
class BankAccount(ABC):
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        self.__balance-=amount
    def getBalance(self):
        return self.__balance
    @abstractmethod
    def interestcalc(self):
        pass
class SavingAccount(BankAccount):
    def interestcalc(self):
        return self.__balance*0.05'''
    

# Inheritance
# Polymorhism
class Animal:
    print("Animal Sound")
class Dog(Animal):
    def sound(self):
        print("Woof")
class Cat(Animal):
    def sound(self):
        print("Meow")