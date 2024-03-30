Big_data_fee=800
Azure_fee=600
Big_data_enrollments=50
Azure_enrollments=40

#calculation is based on BODMAS rule i.e. Brackets, order, division, multiplication,addition and subtraction

total_revenue=(Big_data_fee*Big_data_enrollments)+(Azure_enrollments*Azure_fee)
print(f"the total revenue is {total_revenue}")

# we are now going to calculate average order price

Average_order_price=((Big_data_fee*Big_data_enrollments)+(Azure_enrollments*Azure_fee))/(Big_data_enrollments+Azure_enrollments)

print(f"the average order price is {Average_order_price}")

print(5+3*8)
print ((5+3)*8)
print (18/4)
print(int(18/4))
print (18//4)
print(4**3)
print(2**3**3)
#here in the above code it is right to left i.e 3 to the power 3 is 27 and 2 to the power 27 is 134217728
#the above code is also called right side binding
#hike the fees by 50 dollars
#Big_data_fee= Big_data_fee+50
Big_data_fee+=50
print(Big_data_fee)
