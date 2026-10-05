items = {
    "Cola 25 ML": 25,
    "Cola 100 ML": 85,
    "Sprite 25 ML": 20,
    "Sprite 100 ML": 80,
    "Milk 500 ML": 45,
    "Milk 1L": 95,
    "Chocolate Cookies": 75,
    "Sugar Cookies": 72,
    "Coconut Cookies": 70,
    "Cooking Oil 1L": 150,
    "Cooking Oil 500 ML": 80
}

search_item = input("Enter the item you want to search for: ")
if search_item in items:
    print(f"The item costs BDT {items[search_item]}")
else:
    new_item_price = int(input("Item not found. Please enter the price for the new item: "))
    items[search_item] = new_item_price

    print(f"Item added with price BDT {new_item_price}")
    
    print("Updated items list:")
    for item, price in items.items():
        print(f"{item}: BDT {price}")