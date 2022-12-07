+3

n=15
c=0
for i in range(1,21):
    if(n%i==0):
        c=c+1
        break
    if(c==0):
        print("prime")
    else:
        print("not prime")
        
