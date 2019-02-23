string=input("enter the string=")
vowels=cons=digits=spec=0
for char in str:
    if char in "aeiouAEIOU":vowels+=1
    if char in "bBcCdfFgGhHjJkKlLmMnNpPqQrRsStTuUvVxXyYzZ":CONS=+1
    if char in "0123456789":digits+=1
    if char in "#$@":spec+=1

print("vowels",vowels)
print("cons",cons)
print("digits",digits)
print("special character",spec)
