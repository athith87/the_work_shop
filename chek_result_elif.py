#to check the marks and assign the grade/class
marks=input("enter the marks\n")

marks=int(marks)

if (marks>80):
    print('you have got destinction')
elif(marks>35):
    print('you have passed but not got destinction')
else:
    print('you have failed! put more efforts')

Mat_marks=input("enter the mat marks")
Mat_marks=int(Mat_marks)
if(Mat_marks>=50):
    print('you have passed in second class')

if(Mat_marks>35):
    print('you have passed')
else:
    print('you failed')