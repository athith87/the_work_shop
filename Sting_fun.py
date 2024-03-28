first_name= 'Athith'
last_name= 'K'

print(first_name+' '+ last_name)
print ("my first name is " +first_name+ "last name is " +last_name+ "")

print("----------"*9)
print("my first name is "+first_name+ "last name is "+last_name )
print("---------"*9)
#taking input in python
Name=input("what is your name\n")
print(Name)
Salary=input("what is your salary?\n")
print(Salary)
print(type(Salary))
Salary_hike=input("what is the hike?\n")
print(type(Salary_hike))
Revised_salary=int(Salary)+(int(Salary)*int(Salary_hike)/100)
print("New salary after hike is :", Revised_salary)