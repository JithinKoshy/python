def calc(a,b):
   sum=a+b
   diff=a-b
   mul=a*b
   div=a/b
return sum,diff,mul,div            #return
a=int(input("enter a:"))
b=int(input("enter b:"))
tuple=calc(a,b)                    #tuple
print("sum="tuple[0])
print("diff="tuple[1])
print("mul="tuple[2])
print("div="tuple[3])

