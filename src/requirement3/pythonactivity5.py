
n = (input("Enter name: "))
p = float(input("Enter grade in Physics: "))
a = float(input("Enter grade in Algebra: "))
py = float(input("Enter grade in Programming: "))

ave = (p+a+py)/3

if 75 >= ave:
    stat = ("Failure")

elif 78 <= ave <= 82:
    stat = ("Fair")

elif 83 <= ave <= 88:
    stat = ("Average Student")

elif 89 <= ave <= 94:
    stat = ("Dean Lister")

elif 95 <= ave <= 100:
    stat = ("President Lister")

elif 100 <= ave:
    print("Invalid Grade")

print(f"{n}'s average grade is {ave}")
print(stat)