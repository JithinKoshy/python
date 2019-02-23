#no of lines method 1
'''file1=input("enter sourse file=")
countines=0
fr=open(file1,"r")
for line in fr.readlines():
    countline+=1
fr.close()
print("no of lines",countlines)'''

#no of lines method2
'''file1=input("enter sourse file=")
fr=open(file1,"r")
print("no of lines",len(fr.readlines()))
fr.close()'''

#word count in file
file1=input("enter sourse file=")
fr=open(file1,"r")
wordcount={}
for word in fr.read().split():
    if word  not in wordcount:
        wordcount[word]=1
    else:
        wordcount[word]+=1
for k,v in wordcount.items():
    print(k,"=",v)
fr.close()
