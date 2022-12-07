'''def minicalculator():
    for i in range (20):
        a=int(input("ENTER THE NUMBER: "))
        b=int(input("ENTER THE NUMBER: "))
        symbol=input()
        if symbol=="+":
            print(a+b)
        elif symbol=="*":
            print(a*b)
        elif symbol=="-":
            print(a-b)
        elif symbol=="/":
            print(a/b)
        elif symbol=="//":
            print(a//b)
        elif symbol=="**":
            print(a**b)
        elif symbol=="%":
            print(a%b)
        else:
            print("invalid")
        i=i+1
minicalculator()
'''

'''l1=[1,2,3,4,5,6,7,8,9,23,54,65,72,86,90]
for i in l1:
    print(end=",")
    print(i,end=",")
    a=i
    r=0
    while(a>0):
        l=a%10
        r=(r*10)+l
        a=(a//10)
        print(r)
    if (r==a):
        print("palindrone")
    else:
        print("not palindrone")
    print("max value:",max(l1))
    print("min value:",min(l1))
'''
a=100
def d():
    global a
    print(a)
    a=20
d()
print(a)
