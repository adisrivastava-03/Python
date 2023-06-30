class Stud:
    coll="UCER"
    def __init__(self,name,section):
        self.name=name
        self.section=section

    def printdata(self):
        print("Given Name & Section are ",self.name,"&",self.section,"of",Stud.coll)


s=Stud("ADITYA RANJAN SRIVASTAVA","G")
s.printdata()

print()

class Car:
    def __init__(self):
        self.speed=100
        self.gears=6

c1=Car()
c2=Car()
c1.speed=120
c2.gears=7
print(c1.speed," ",c1.gears)
print(c2.speed," ",c2.gears)

print()
print("Cocept of INHERITANCE")
class A1:
    def f1(self):
        print("F1 is Working")
    def f2(self):
        print("F2 is Working")

class B1(A1):
    def f3(self):
        print("F3 is Working")
    def f4(self):
        print("F4 is Working")

class C(B1):
    def f5(self):
        print("F5 is Working")

obj=C()
obj.f1()
obj.f3()
obj.f5()
print("\n")


class a():
    def fn1(self):
        print("Function 1 executed")
class b():
    def fn2(self):
        print("Function 2 executed")
class c():
    def fn3(self):
        print("Function 3 executed")

class All(a,b,c):
    __a = 999
    def name(self):
            #private encapsulation
        print(self.__a)
        print("MULTIPLE  INHERITENCE")

o=All()
o.fn1()
o.fn2()
o.fn3()
o.name()
