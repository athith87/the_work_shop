order=[1, "23-03-2023 00:00:0", 11599, "CLOSED"]
print(order)
print(type(order))
print(order[3])
print(order[2])
print(order[1])
print(order[0])
order.append(100)
print(order)
order.insert(3, "OPEN")
print(order)
""" if it is in square bracket then it is a list """
