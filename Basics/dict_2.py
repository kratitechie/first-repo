print("Details of a product:\n")
product={
    'name': 'Laptop',
    'price': 69000,
    'brand': 'Dell'
}



for k, v in product.items():
    print (k,":",v)


new_price=int(input("Enter the new price of the product: "))
product['price']=new_price

print("\nUpdated product details are:\n")
for k,v in product.items():
   print(k,":",v)