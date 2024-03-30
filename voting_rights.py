#To check if citizen has voting rights
Age=input("enter the age of the citizen:\n")
Criminal_case=input("does the citizen has any criminal cases:\n")

Age=int(Age)

if(Age>=18 and Criminal_case=="no"):
    print("the citizen is eligible to vote")
else:
    print("the citizen is not eligible to vote")

name="athith k"

print("athith" in name)

