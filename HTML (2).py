'''n=123
r=0
s=0
n1=n
while(n>0):
    l=n%10
    r=(r*10)+l
    s1=s+1
    s2=s+(l**3)
    n=n//10
    print("reverse of",n,"is",r)
if(n==r):
    print("palidrome")
else:
    print("not palidrome")
    print("armstrong of",n,"is",s2)
    print("sum of all digits of",n,"is",s1)
'''

'''a=int(input())
c=0
for i in range (2,a):
    if(a%i==0):
        c=c+1
        break
if(c==0):
    print("Prime")
else:
    print("Not Prime")
'''


'''s=0
i=1
while(i<+21):
    n=int(input("enter n: "))
    i=i+1
    if(n<0):
       continue
    s=s+n
    print(s)
        
'''

'''str="Harsh@123"
digit=letter=upper=lower=0
for ch in str:
    if(ch>="0" and ch<="9"):
        digit=digit+1
    elif(ch>="a" and ch<="z"):
        lower=lower+1
    else:
        (ch>="A" and ch<="Z")
        upper=upper+1
print("lower",lower)
print("upper",upper)
print("digit",digit)
            
'''


'''x=int(input("enter any no."))
y=int(input("enter any 2nd no."))
if x>y:
    smaller=y
else:
    smaller=x
for i in range(1,smaller+1):
    if((x%i==0) and (y%i==0)):
        hcf=i
print("The H.C.F is",hcf)        
    
'''




n=10
for i in range (1, n+1):
    #interval loop run for i times
    for k in range(1, i+1):
        print(k , end=" ")
    print()    
    

     

        
    
    
