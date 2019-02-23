list=[1,83,90,67,54]
num=int(input("enter the number"))
for item in range(len(list)):
    if list[item]==num:
        print("item fount")
        break
else:print("item not fount")
