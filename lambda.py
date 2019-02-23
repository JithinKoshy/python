'''oldlist=[10,21,31,40,50,61]
print(oldlist)
newlist=list(map(lambda x:x+2,oldlist))
print(newlist)'''


'''oldlist=[10,21,31,40,50,61]
print(oldlist)
newlist=list(filter(lambda x:x%2!=0,oldlist))
print(newlist)'''


import functools
oldlist=[10,21,31,40,50,61]
print(oldlist)
sum=functools.reduce(lambda x,y,x+y,oldlist)
print(sum)
