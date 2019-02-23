choice=0
a,b=6,3
while choice!=5:
    print("1.sum")
    print("2.diff")
    print("3.exit")
    choice=int(input("enter your choice:"))
    if choice==1:print(a+b)
    if choice==2:print(a-b)
    if choice==3:break
