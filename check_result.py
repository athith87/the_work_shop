#to check the result
marks=input("enter the marks\n")

marks=int(marks)

if marks>=35:
    if marks>=80:
        print("you have passed in distinction")
    else:
        print("you passed but not distinction")
else:
    print("hard luck you failed!")
