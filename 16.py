s,k=map(int,input().split())
for num in range(s,k+1):
   if num>1:
     for i in range (2,num):
        if(num%i)==0:
           break
     else:
              print(num,end=" ")
