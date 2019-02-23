import re 
p=input("enter your password")
while True:   
    if len(p)<6 or len(p)>16:
        print("Not a Valid Password") 
        break
    elif not re.search("[a-zA-Z0-9]", p): 
        print("Not a Valid Password") 
        break
  
    elif not re.search("[_@$]", p):
        print("Not a Valid Password") 
        break
    else: 
        print("Valid Password") 
        break
