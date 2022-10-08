product = input("Enter Product: ")
price = float(input("Enter Price: "))

if 0 <= price <= 10000:
    discount = float('0')

elif 10001 <= price <= 20000:
    discount = float('0.05')

elif 20001 <= price <= 50000:
    discount = float('0.10')

elif 50001 <= price <= 100000:
    discount = float('0.15')

elif 100001 <= price:
    discount = float('0.20')

else:
    print("Invalid Price")

discountP = (price*discount)
netprice = (price-discountP)

print("Price of modem router is",price)
print("Discount is", discountP)
print("Net Price is", netprice)