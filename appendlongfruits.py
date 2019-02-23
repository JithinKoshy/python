str=input("enter the words=")
fruits=str.split()
n=int(input("enter the length"))
longfruits=[]
for fruit in fruits:
    if len(fruit)>n:
        longfruits.append(fruit)
print("fruits longer than",n,"is",longfruits)
