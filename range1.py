'''list=[x for x in range(1,20,2)]
print(list)'''

list=[(x,y,z)for x in range(1,20)for y in range (x,20)for z in range (y,20)if z*z==x**2+y**2]
print(list)
