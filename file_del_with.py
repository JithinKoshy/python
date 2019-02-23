def filedel(str,n):
    with open(str,"r")as file:
        list=file.readlines()
        del list[n]
        file.close()
    with open(str,"w") as file:
        file.writelines(list)
        file.close()

str=input("enter a file")
n=int(input("enter position"))
filedel(str,n)
