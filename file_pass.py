import os
def filedel(str,word):
    file=open(str,"r")
    newfile=open("new.txt","w")
    while True:
        line=file.readline()
        if not line:
            break
        elif word in line:
            pass
        else:
            newfile.write(line)
    file.close()
    newfile.close()
    os.remove(str)
    os.rename("new.txt",str)


str=input("enter a file:")
word=input("enter a word:")
filedel(str,word)
