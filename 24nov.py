'''class Area:
    def __init__(self):
        self.r=int(input())

    def circle(self):
        print(3.14*self.r*self.r)

ob1=Area()
ob1.circle()
ob2=Area()
ob2.circle()




class Info:
    def __init__(self ,a,b):
        self.name=a
        self.age=b
    def display(self):
        print("name: ",name)
        print("age: ",age)

c1=Info(a,b)
c1.display()




#single level inheritance
class Furniture:
    def p1(self):
        print("This is a Furniture")
class Table(Furniture):
    def p2(self):
        print("This is a Table")
b=Table()
b.p2()
b.p1()




#multi level inheritance
class Furniture:
    def p1(self):
        print("This is a Furniture")
class Table(Furniture):
    def p2(self):
        print("This is a Table")
class Chair(Table):
    def p3(self):
        print("This is a Chair")
b=Chair()
b.p3()
b.p2()
b.p1()




#multiplelevel inheritance
class Calc1:
    def Sum(self,a,b):
        return a+b
class Calc2:
    def Multiply(self,a,b):
        return a*b
class Derived(Calc1,Calc2):
    def Divide(self,a,b):
        return a/b
d=Derived()
print(d.Sum(10,30))
print(d.Multiply(10,30))
print(d.Divide(10,30))
'''


