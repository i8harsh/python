"""#fibnoci series
n=int(input())
a=0
b=1
print(a,b)
for i in range(3,n+1):
    s=a+b
    print(s)
"""

"""n=int(input())
def fib(n):
    if(n==1):
        return 1
    elif(n==2):
        return 2
    else:
        return(fib(n-1)+fib(n-2))
n=int(input())
for i in range(1,n+1):
    print(fib(i))
"""
"""
# reverse of 1 to 10
l = [1,2,3,4,5,6,7,8,9,10]
def recursive(l):
    if len(l) == 0:
        return []
    else:
        return [l.pop()] + recursive(l)
print(recursive(l))"""

n=input()
def rev(n):
    if n==1:
        print(n)
    else:
        print(n)
        rev(n-1)
    rev(n)
