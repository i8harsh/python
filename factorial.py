#sum of positive 5 nos.and terminate at negative number
i=1
s=0
while i<6:
   n=int(input("enter the value"))
      if(n<0):
    break
s=s+n
i+=1


print(s)

#sum of positive number and egnore negative
i=1
s=0
while i<6:
   n=int(input("enter the value"))
    i+=1
     if(n<0):
     continue
s=s+n
print(s)
    

    
