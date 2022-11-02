from tabulate import *
data = []
def sales(y):
    return number[0] + number[1] + number[2] + number[3] + number[4]
number = [ ]

data.insert(0, str(input("Enter athlete : ")))
number.insert(0, float(input("Enter sales: ")))

data.insert(1, str(input("Enter athlete : ")))
number.insert(1, float(input("Enter sales: ")))

data.insert(2, str(input("Enter athlete : ")))
number.insert(2, float(input("Enter sales: ")))

data.insert(3, str(input("Enter athlete : ")))
number.insert(3, float(input("Enter sales: ")))

data.insert(4, str(input("Enter athlete : ")))
number.insert(4, float(input("Enter sales: ")))


result = sales(number)

print(data)
print(number)
print(f"Total ${result}")



