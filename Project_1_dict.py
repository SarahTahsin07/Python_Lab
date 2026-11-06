prices ={
    "rice" : 75,
    "oil" : 185,
    "sugar" : 120,
    "milk" : 95,
    "egg" : 12,
    "flour" : 65,
    "salt" : 40,
    "lentil" : 130,
    "potato" : 45,
    "onion" : 80,
    "tea" : 250,
    "coffee" : 450,
    "biscuit" : 50,
    "soap" : 70,
    "shampoo" : 180
}                                               #the original dict of products

print("======== AVAILABLE PRODUCTS ========")
print("Item\t\tPrice")
print("=" *36)
for item in prices:                             #print the available products and their prices
    print(f"{item}\t\t{prices[item]}")
print("=" *36)

while True:                                     #to check valid user input for number of orders
    order_num = int(input("How many order entries? "))
    if order_num <= 0:
        print("Please enter a valid number of entries.")
        continue
    else:
        break

order = {}                                       #will contain the user products and quantities
for i in range(order_num):
    product_name = input(f"Enter product {i+1}: ").lower()
    product_quantity = int(input(f"Enter quantity: "))
                                  #take product name

    if product_name not in prices:
        print(f"{product_name} is not available.") #available or not
    elif product_quantity <= 0:
        print("Please enter a valid quantity.")    #avoild neg and zero

    else:                                          #get() method used as per instructions
        order[product_name] = order.get(product_name, 0) + product_quantity

print("Final order:")
print(order)                                       #show order dict

bill = {}
subtotal = 0

for product_name, product_quantity in order.items():
    unit_price = prices[product_name]              #get the unit price of the product
    total = product_quantity * unit_price

    bill[product_name] = {                         #to keep billing info
        "quantity": product_quantity,
        "unit_price": unit_price,
        "total": total
    }
    subtotal += total

if subtotal >= 1000:
    discount = subtotal*0.5                        #apply 5% discount when applicable
else:
    discount = 0

vat = 0.02 * (subtotal - discount)                 #calculate 2% vat
final_amount = subtotal - discount + vat           #calculate final amount

#Final bill printout
print("\n================ GROCERY SHOP BILL ================")
print(f"{'Item':<15}{'Quantity':<10}{'Unit Price':<15}{'Total':<10}")
print("-"*51)

for product_name, product_info in bill.items():
    print(f"{product_name:<15}{product_info['quantity']:<10}{product_info['unit_price']:<15.2f}{product_info['total']:<10.2f}")

print("-"*51)

print(f"{'Subtotal:':<38} Tk {subtotal:<10.2f}")
print(f"{'Discount (5%):':<38} Tk {discount:<10.2f}")
print(f"{'VAT (2%):':<38} Tk {vat:<10.2f}")

print("-"*51)
print(f"Final amount: Tk {final_amount:<10.2f}")
print("="*51)