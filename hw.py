Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
test={}
print(type(test))
<class 'dict'>
t=set()
print(type(t))
<class 'set'>
tuple1=tuple()
print(tuple1)
()
mytuple=(1,2,3,"datatypes")
print(mytuple)
(1, 2, 3, 'datatypes')
print(type(mytuple))
<class 'tuple'>
mytuple=
SyntaxError: invalid syntax
mytuple=(1)
print(mytuple)
1
print(type(mytuple))
<class 'int'>
mytuple=(1,)
print(mytuple)
(1,)
print(type(mytuple))
<class 'tuple'>
a=12
print("%5d"%a)
   12
a=2346
print("%2d"%a)
2346
a=234
print("%6d"%a)
   234
a=12
b=12.457
c="hello"
print("%5d%.2f%7s"%(a,b,c))
   1212.46  hello
a=12
b=34.5897
print("The value of a is:{0:3f}".format(b))
The value of a is:34.589700
a=34.6892
print("a=%f"%a)
a=34.689200
print("a=%.3f"%a)
a=34.689
print("value of a=",a'"and b=",b)
      
SyntaxError: unterminated string literal (detected at line 1)
print("value of a=",a,"and b=",b)
      
value of a= 34.6892 and b= 34.5897
print("value of a={} and b={}".format(a,b))
      
value of a=34.6892 and b=34.5897
print("value of a is {0:.2f}".format(a))
      
value of a is 34.69
print("value of a = %f and b= %.d"%(a,b))
      
value of a = 34.689200 and b= 34
a=3
      
b=10
      
print("Tow values are {} and {}".format(a,b))
      
Tow values are 3 and 10
print("Two values are {1} and {0}".format(a,b))
      
Two values are 10 and 3
a=1
      
b=2
      
a,b=eval(input("enter a,b"))print(a,b)
      
SyntaxError: invalid syntax
print(a,b)
      
1 2
d1={"hyderabad":27,"chennai":32,"mumbai":40}
      
d1={"A":3,"C":4,"D":3}
      
d1=dict(abc:20,xyz:40
        
SyntaxError: invalid syntax
d1=dict(abc:20,xyz:40)
        
SyntaxError: invalid syntax
d2={"abc":20,"xyz":40}
        
print(d2[xyz])
        
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    print(d2[xyz])
NameError: name 'xyz' is not defined
print(d2["xyz"])
        
40
mydict=dict()
        
print(mydict)
        
{}
print(ord('z'))
        
122
print(ord('Z'))
        
90
print(ord('a'))
        
97
print
        
<built-in function print>
print(ord("A"))
        
65
