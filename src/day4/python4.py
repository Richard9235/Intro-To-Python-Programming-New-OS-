numbers = []
ctr = 0
while ctr < 20:
    num = int(input(f"Enter number {ctr+1}: "))
    numbers.insert(ctr, num)
    ctr += 1

print("Loop Done")
print("Displaying Input")
print(numbers)