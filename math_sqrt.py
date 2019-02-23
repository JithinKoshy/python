import math
m=int(input("1st limit"))
n=int(input("2nd limit"))
for i in range(m,n+1):
    k=int(math.sqrt(i))
    for j in range(2,k+1):
        if i%j==0:break
    else:print(i)
