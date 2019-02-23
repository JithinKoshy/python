file1=input("enter sourse file=")
file2=input("enter destination file=")
fr=open(file1,"r")
fw=open(file2,"w")
for line in fr.readlines():
    fw.write(line)
fr.close()
fw.close()
