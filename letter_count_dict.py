str=input("enter a string =")
counts={}
for char in str:
    if char not in counts:
        counts[char]=1
    else:
        counts[char]+=1
for k,v in counts.items():
    print(k,"=",v)
