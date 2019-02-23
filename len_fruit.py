str=input("enter a fruits:")
fruits=str.split()
wordlen=[]
for fruit in fruits:
    wordlen.append((len(fruit),fruit))
wordlen.sort()
print("longest is",wordlen[-1][1],"and its length",wordlen[-1][0])
