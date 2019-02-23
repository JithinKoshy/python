import os
def filesearchandreplace(str,oldword,newword):
    file=open(str,"r")
    newfile=open("new.txt","w")
    while True:
        line=file.readline()
        if not line:
            break
        
        else:
            newfile.write(line.replace(oldword,newword))
    file.close()
    newfile.close()
    os.remove(str)
    os.rename("new.txt",str)


str=input("enter a file:")
oldword=input("enter a word to be replaced:")
newword=input("enter a word:")
filesearchandreplace(str,oldword,newword)
