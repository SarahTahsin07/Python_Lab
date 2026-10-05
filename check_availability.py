items = ["banana", "Apple", "orange", "grape", "kiwi", "mango"]

input_item = input("Enter an item to check availability: ").lower()

for item in items:
    item = item.lower()
    if item == input_item:
        print(f"{input_item} is available.")
        break
    else:
        print(f"{input_item} is not available.")
        items.append(input_item)
        print(f"Updated item list: {items}")
        break
        