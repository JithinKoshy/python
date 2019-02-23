class Student:
    def getdata(self,rollno,name):
        self.rolno=rollno
        self.name=name
        def displayStudent(self):
            print("Roll no:",self.rollno)
            print("name",self.name)
    
class Test(Student):
    def getMarks(self,marks):
        self.marks=marks
    def putMarks(self):
        print("marks:",self.marks)
        
r=int(input("enter the roll no:"))
n=input("enter name")
m=int(input("enter marks:"))
stud1=Test()
stud1.getData(r,n)
stud1.getMarks(m)
stud1.displayStudent()
stud1.putMarks()
