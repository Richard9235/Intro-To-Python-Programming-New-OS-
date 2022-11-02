def perim(x, y):
    return 2 *(x+y)

def area(x, y):
    return x*y

len = float(input("Enter Length: "))
wid = float(input("Enter Width: "))

areareal = area(len, wid)
perimeter = perim(len, wid)

print(f"Perimeter is {perimeter} meters")
print(f"Area is {areareal} meters")