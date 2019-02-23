'''from math import*
print(sqrt(100))
print(floor(98.64))'''


import math
def prime(n):
    for j in range(2,int(math.sqrt(n))+1):
    if n%j==0:break
   else:return True


