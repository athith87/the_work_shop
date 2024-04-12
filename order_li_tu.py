order_list=[1, "2013-07-03 12:00:0", 11599, "CLOSED" ]
order_tuple=(1, "2013=-7-01 13:00:0", 11599, "Closed")
print(order_list)
order_list.insert(2, "Ben")
print(order_tuple)
print(order_list)
for x in order_list:
    print(x)
print("list is printed")

for x in order_tuple:
    print(x)
print("tuple is printed")
for x in order_list:
    print(x)
for x in order_list:
    print(type(order_list))
for x in order_tuple:
    print(type(order_tuple))